from django.shortcuts import render, redirect
from booktest.models import BookInfo
from datetime import date
# from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    """显示图书信息"""
    books = BookInfo.objects.all()

    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    # 创建BookInfo对象
    b = BookInfo()
    b.btitle = '斗破苍穹'
    b.bpub_date = date(1994, 11, 6)
    b.bread = 100
    b.bcomment = 200
    b.isDelete = False
    b.save()
    # return HttpResponseRedirect('index')
    return redirect('/index')


def delete(request, bid):
    """删除点击的图书"""
    book = BookInfo.objects.get(id=bid)
    book.delete()
    # return HttpResponseRedirect('index')
    return redirect('/index')





