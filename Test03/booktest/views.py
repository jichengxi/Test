from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')


def login(request):
    """显示ajax登录页面"""
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
        password = request.session['password']
    else:
        username = ''
        password = ''

    return render(request, 'booktest/login.html',{'username':username, 'password':password})


def login_check(request):
    """登录校验"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    if username == 'jichengxi' and password == '123456':
        response = JsonResponse({'res': 1})
        if remember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)
            request.session['password'] = password
            return response
    else:
        return JsonResponse({'res':0})
