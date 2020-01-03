from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.


def index(request):
    # 进行处理
    # return HttpResponse('123456')

    # # 使用模版文件
    # # 1. 加载模版文件
    # temp = loader.get_template('booktest/index.html')
    # # 2. 定义模版上下文：给模版传递数据
    # context = {}
    # # 3. 模版渲染，产生标准的html内容
    # res_html = temp.render(context)
    # # 4. 返回给浏览器
    # return HttpResponse(res_html)
    return render(request, 'booktest/index.html', {})


def love(request):
    # 进行处理
    return HttpResponse('我爱吴婷婷')

