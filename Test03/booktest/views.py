from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')


def login(request):
    """显示ajax登录页面"""
    return render(request, 'booktest/login.html')


def login_check(request):
    """登录校验"""
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == 'jichengxi' and password == '123456':
        return JsonResponse({'res':1})
    else
        return JsonResponse({'res':0})
