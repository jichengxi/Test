from celery import Celery
from django.conf import settings
from django.core.mail import send_mail
import time

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TTShengXian.settings')
django.setup()


# 创建celery类的实例对象
task0 = Celery('celery_tasks.tasks', broker='redis://192.168.0.250:6379/0')


# 定义任务函数
@task0.task
def send_register_active_email(to_email, username, token):
    # 发送邮件
    subject = '天天生鲜欢迎信息'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '<h1>%s 欢迎您成为天天生鲜注册会员</h1>请点击<a href="http://127.0.0.1:8000/user/active/%s">激活</a>您的账户<br/>' % (
        username, token)

    send_mail(subject, message, sender, receiver, html_message=html_message)
    time.sleep(7)
