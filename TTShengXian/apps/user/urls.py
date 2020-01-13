from django.urls import path,re_path
from apps.user import views
from apps.user.views import RegisterView, ActiveView, LoginView

urlpatterns = [
    # path('register', views.register, name='register'),
    path('register', RegisterView.as_view(), name='register'),  # 注册
    re_path(r'active/(?P<token>.*)', ActiveView.as_view(), name='active'),  # 用户激活
    path('login', LoginView.as_view(), name='login')  # 登录
]
