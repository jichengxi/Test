from django.urls import re_path, path
from booktest import views

urlpatterns = [
    # 通过url函数设置url路由配置项
    path('index', views.index),
    path('love', views.love)
]
