from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse
from apps.user.models import User, Address
from apps.goods.models import GoodsSKU
from django.conf import settings
from django.core.mail import send_mail
import re
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from celery_tasks.tasks import send_register_active_email
from django.contrib.auth import authenticate, login, logout
from utils.mixin import LoginRequiredMixin
from django_redis import get_redis_connection


# Create your views here.

"""
def register(request):
    # 注册页面
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        cpassword = request.POST.get('cpwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 校验数据
        if not all([username, password, cpassword, email, allow]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        if password != cpassword:
            return render(request, 'register.html', {'errmsg': '密码不一致'})

        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        try:
            user = User.objects.get(username=username)
            return render(request, 'register.html', {'errmsg': '用户名已存在'})
        except User.DoesNotExist:
            # 用户名不存在
            # 注册
            user = User.objects.create_user(username, email, password)
            user.is_active = 0
            user.save()

            return redirect(reverse('goods:index'))
"""


class RegisterView(View):
    """注册类视图"""

    def get(self, request):
        """显示注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """注册账户"""
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        cpassword = request.POST.get('cpwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 校验数据
        if not all([username, password, cpassword, email, allow]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        if password != cpassword:
            return render(request, 'register.html', {'errmsg': '密码不一致'})

        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        try:
            user = User.objects.get(username=username)
            return render(request, 'register.html', {'errmsg': '用户名已存在'})
        except User.DoesNotExist:
            # 用户名不存在
            # 注册
            user = User.objects.create_user(username, email, password)
            user.is_active = 0
            user.save()

            # 激活
            # 加密
            serializer = Serializer(settings.SECRET_KEY, 3600)
            info = {'confirm': user.id}
            token = serializer.dumps(info)
            # 转义
            token = token.decode()

            # 发邮件
            send_register_active_email.delay(email, username, token)

            # subject = '天天生鲜欢迎信息'
            # message = ''
            # sender = settings.EMAIL_FROM
            # receiver = [email]
            # html_message = '<h1>%s 欢迎您成为天天生鲜注册会员</h1>请点击<a href="http://127.0.0.1:8000/user/active/%s">激活</a>您的账户<br/>' % (
            #     username, token)
            #
            # send_mail(subject, message, sender, receiver, html_message=html_message)

            return redirect(reverse('goods:index'))
            # return HttpResponse('ok')


class ActiveView(View):
    """用户激活"""

    def get(self, request, token):
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            user_id = info['confirm']
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            return HttpResponse('激活链接已过期')


class LoginView(View):
    """登录页面"""

    def get(self, request):
        # 判断是否记录了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''

        return render(request, 'login.html', {'username': username, 'checked': checked})

    def post(self, request):
        """登录校验"""
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 校验
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        # 登录验证
        # https://docs.djangoproject.com/zh-hans/3.0/topics/auth/default/
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            if user.is_active:
                # 记录登录状态
                login(request, user)

                # 获取登录后所要跳转的地址
                # 默认跳转到首页
                next_url = request.GET.get('next', reverse('goods:index'))  # None

                # # 跳转到首页
                response = redirect(next_url)

                # 判断是否需要记住用户名
                remember = request.POST.get('remember')
                if remember == 'on':
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('username')

                return response




            else:
                return render(request, 'login.html', {'errmsg': '用户未激活'})
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})


class LogoutView(View):
    """注销登录"""

    def get(self, request):
        logout(request)
        return redirect(reverse('goods:index'))


# /user
class UserInfoView(LoginRequiredMixin, View):
    def get(self, request):
        # 获取用户的个人信息
        user = request.user
        address = Address.objects.get_default_address(user)
        # 获取用户的浏览记录
        # from redis import StrictRedis
        # sr = StrictRedis(host='192.168.0.250', port='6379', db=1)
        con = get_redis_connection('default')
        history_key = 'history_%d' % user.id
        # 获取用户最新获取的5个商品的id
        sku_ids = con.lrange(history_key, 0, 4)

        # 遍历获取用户浏览的商品信息
        goods_li = []
        for id in sku_ids:
            goods = GoodsSKU.objects.get(id=id)
            goods_li.append(goods)

        # 组织上下文
        context = {'page': 'user', 'address': address, 'goods_li': goods_li}
        return render(request, 'user_center_info.html', context)


# /user/order
class UserOrderView(LoginRequiredMixin, View):
    def get(self, request):
        # 获取用户的订单信息
        return render(request, 'user_center_order.html', {'page': 'order'})


# /user/site
class UserSiteView(LoginRequiredMixin, View):
    def get(self, request):
        # 获取用户的默认收货地址
        user = request.user
        address = Address.objects.get_default_address(user)

        return render(request, 'user_center_site.html', {'page': 'site', 'address': address})

    def post(self, request):
        """地址的添加"""
        # 接收数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        # 校验数据
        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html', {'errmsg': '数据不完整'})

        if not re.match(r'^1[3|4|5|7|8][0-9]{9}$', phone):
            return render(request, 'user_center_site.html', {'errmsg': '手机格式不正确'})

        # 添加地址
        user = request.user
        address = Address.objects.get_default_address(user)

        if address:
            is_default = False
        else:
            is_default = True

        Address.objects.create(user=user, receiver=receiver, addr=addr, zip_code=zip_code, phone=phone,
                               is_default=is_default)

        return redirect(reverse('user:site'))  # 重新刷新页面 get请求
