from django.shortcuts import render, redirect, HttpResponseRedirect, reverse,HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse

from hashlib import sha1
from .models import GoodsBrowser, UserInfo
from . import user_decorator
from order.models import *


def register(request):

    context = {
        'title': 'user registration',
    }
    return render(request, 'df_user/register.html', context)


def register_handle(request):

    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    confirm_pwd = request.POST.get('confirm_pwd')
    email = request.POST.get('email')

    # Judging the consistency of two passwords
    if password != confirm_pwd:
        return redirect('/user/register/')
    # password encryption
    s1 = sha1()
    s1.update(password.encode('utf8'))
    encrypted_pwd = s1.hexdigest()

    # create object
    UserInfo.objects.create(uname=username, upwd=encrypted_pwd, uemail=email)
    # registration success
    context = {
        'title': 'user login',
        'username': username,
    }
    return render(request, 'df_user/login.html', context)


def register_exist(request):
    username = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=username).count()
    return JsonResponse({'count': count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {
        'title': 'user login',
        'error_name': 0,
        'error_pwd': 0,
        'uname': uname,
    }
    return render(request, 'df_user/login.html', context)


def login_handle(request):
    # accept request information
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 1:  # Determine the user password and jump
        s1 = sha1()
        s1.update(upwd.encode('utf8'))
        if s1.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)  # Inherit and HttpResponse set a cookie value while jumping
            # Whether to check remember user name, set cookie
            red.set_cookie('uname', '', max_age=-1)  # Set expiration cookie time, expire immediately
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {
                'title': 'Login with username',
                'error_name': 0,
                'error_pwd': 1,
                'uname': uname,
                'upwd': upwd,
            }
            return render(request, 'df_user/login.html', context)
    else:
        context = {
            'title': 'Login with username',
            'error_name': 1,
            'error_pwd': 0,
            'uname': uname,
            'upwd': upwd,
        }
        return render(request, 'df_user/login.html', context)


def logout(request):  # user logout
    request.session.flush()  # Clear all sessions of the current user
    return redirect(reverse("df_goods:index"))

def findpassword(request): #retrieve password
    context = {
        'title': 'retrieve password',
    }
    return render(request, 'df_user/findpassword.html', context)
def newpassword(request): #reset Password
    uname = request.POST.get('user_name')
    context = {
        'title': 'retrieve password',
        'user_name':uname
    }
    return render(request,'df_user/newpassword.html',context)


def newpassword2(request,username): #reset Password
    uname = username
    context = {
        'title': 'retrieve password',
        'user_name':uname
    }
    return render(request,'df_user/newpassword.html',context)


def newpassword_handle(request):
    username = request.POST.get('user_al')
    password = request.POST.get('pwd')
    confirm_pwd = request.POST.get('confirm_pwd')

    # Judging the consistency of two passwords
    if password != confirm_pwd:
        return redirect('/user/login/')
    # password encryption
    s1 = sha1()
    s1.update(password.encode('utf8'))
    encrypted_pwd = s1.hexdigest()

    # update object
    try:
        UserInfo.objects.get(uname=username,)
    except UserInfo.DoesNotExist:
        old = UserInfo()
        old.upwd = encrypted_pwd
        old.save()
    # registration success
    context = {
        'title': 'user login',
        'username': username,
    }
    return render(request, 'df_user/login.html', context)

@user_decorator.login
def info(request):  # User Center
    username = request.session.get('user_name')
    user = UserInfo.objects.filter(uname=username).first()
    browser_goods = GoodsBrowser.objects.filter(user=user).order_by("-browser_time")
    goods_list = []
    if browser_goods:
        goods_list = [browser_good.good for browser_good in browser_goods]  # Retrieve the browsed product from the browsed product record
        explain = 'Recently Viewed'
    else:
        explain = 'no recent view'

    context = {
        'title': 'User Center',
        'page_name': 1,
        'user_phone': user.uphone,
        'user_address': user.uaddress,
        'user_name': username,
        'goods_list': goods_list,
        'explain': explain,
    }
    return render(request, 'df_user/user_center_info.html', context)


@user_decorator.login
def order(request, index):
    user_id = request.session['user_id']
    orders_list = OrderInfo.objects.filter(user_id=int(user_id)).order_by('-odate')
    paginator = Paginator(orders_list, 5)
    page = paginator.page(int(index))
    context = {
        'paginator': paginator,
        'page': page,
        # 'orders_list':orders_list,
        'title': "User Center",
        'page_name': 1,
    }
    return render(request, 'df_user/user_center_order.html', context)


@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == "POST":
        user.ushou = request.POST.get('ushou')
        user.uaddress = request.POST.get('uaddress')
        user.uyoubian = request.POST.get('uyoubian')
        user.uphone = request.POST.get('uphone')
        user.save()
    context = {
        'page_name': 1,
        'title': 'User Center',
        'user': user,
    }
    return render(request, 'df_user/user_center_site.html', context)


@user_decorator.login
def comment(request):
    oid=request.GET.get('oid')
    comment_orde=OrderInfo.objects.filter(oid=int(oid)).first()
    data_order=OrderDetailInfo.objects.filter(order=int(oid)).all()
    info={
        'order_detail':comment_orde,
        'data_order':data_order
    }
    return render(request,'df_user/user_order_comment.html',info)
