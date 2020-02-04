from django.urls import path,re_path
from apps.user import views
from apps.user.views import RegisterView, ActiveView, LoginView,LogoutView, UserInfoView, UserOrderView, UserSiteView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path('register', views.register, name='register'),
    path('register', RegisterView.as_view(), name='register'),  # 注册
    re_path(r'active/(?P<token>.*)', ActiveView.as_view(), name='active'),  # 用户激活
    path('login', LoginView.as_view(), name='login'),  # 登录
    path('logout', LogoutView.as_view(), name='logout'),  # 注销登录

    path('', UserInfoView.as_view(), name='user'),  # 用户中心信息页
    path('order', UserOrderView.as_view(), name='order'),  # 用户中心订单页
    path('site', UserSiteView.as_view(), name='site'),  # 用户中心地址页

]
