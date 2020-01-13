from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse
from apps.user.models import User
from django.conf import settings
from django.core.mail import send_mail
import re
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired


# Create your views here.


def register(request):
    """注册页面"""
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
            serializer = Serializer(settings.SECRET_KEY, 3600)
            info = {'confirm': user.id}
            token = serializer.dumps(info)
            token = token.decode()

            subject = '天天生鲜欢迎信息'
            message = ''
            sender = settings.EMAIL_FROM
            receiver = [user.email]
            html_message = '<h1>%s 欢迎您成为天天生鲜注册会员</h1>请点击<a href="http://127.0.0.1:8000/user/active/%s">激活</a>您的账户<br/>' % (username, token)

            send_mail(subject, message, sender, receiver, html_message=html_message)

            return redirect(reverse('goods:index'))


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
        return render(request, 'login.html')
