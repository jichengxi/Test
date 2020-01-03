from django.contrib import admin
from booktest.models import BookInfo

# Register your models here.
# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ['id', 'bittle', 'bpub_date']

# 注册模型表
admin.site.register(BookInfo, BookInfoAdmin)
