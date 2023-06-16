from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

from datetime import datetime
from decimal import Decimal

from .models import OrderInfo, OrderDetailInfo
from cart.models import CartInfo
from user.models import UserInfo
from user import user_decorator


@user_decorator.login
def order(request):
    uid = request.session['user_id']
    user = UserInfo.objects.get(id=uid)
    cart_ids = request.GET.getlist('cart_id')
    carts = []
    total_price = 0
    for goods_id in cart_ids:
        cart = CartInfo.objects.get(id=goods_id)
        carts.append(cart)
        total_price = total_price + float(cart.count) * float(cart.goods.gprice)

    total_price = float('%0.2f' % total_price)
    trans_cost = 10  # shipping cost
    total_trans_price = trans_cost + total_price
    context = {
        'title': 'Submit Order',
        'page_name': 1,
        'user': user,
        'carts': carts,
        'total_price': float('%0.2f' % total_price),
        'trans_cost': trans_cost,
        'total_trans_price': total_trans_price,
        # 'value':value
    }
    return render(request, 'df_order/place_order.html', context)

'''
Transaction commit:
In these steps, if any link is wrong, all will be returned to 1
1. Create an order object
2. Judging whether the commodity inventory is sufficient
3. Create order details, multiple
4. Modify commodity inventory
5. Delete shopping cart
'''


@user_decorator.login
@transaction.atomic()  # Transaction
def order_handle(request):
    tran_id = transaction.savepoint()  # Save point
    cart_ids = request.POST.get('cart_ids')  # Assign id to shopping cart
    user_id = request.session['user_id']  # Get user id
    data = {}
    try:
        order_info = OrderInfo()  # Create an order object
        now = datetime.now()
        order_info.oid = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), user_id)  # Order number = order time + user id
        order_info.odate = now  # order time
        order_info.user_id = int(user_id)  # The user id of the order
        order_info.ototal = Decimal(request.POST.get('total'))  # Get the total price
        order_info.save()  # Save Order

        for cart_id in cart_ids.split(','):
            cart = CartInfo.objects.get(pk=cart_id)  # Get the cart object from the CartInfo table
            order_detail = OrderDetailInfo()  # Every small item order in a large order
            order_detail.order = order_info  # Foreign key association, small order and large order binding
            goods = cart.goods  # select product
            if cart.count <= goods.gkucun:  # Determine whether the inventory meets the order, and if so, modify the database
                goods.gkucun = goods.gkucun - cart.count
                goods.save()
                order_detail.goods = goods
                order_detail.price = goods.gprice
                order_detail.count = cart.count
                order_detail.save()
                cart.delete()  # Delete cart
            else:  # else, order canceled
                transaction.savepoint_rollback(tran_id)
                return HttpResponse('Out of Stock')
        data['ok'] = 1
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print("%s" % e)
        print('Incomplete submission')
        transaction.savepoint_rollback(tran_id)  # Error in link, cancel all
    return JsonResponse(data)


@user_decorator.login
def pay(request):
    pass
