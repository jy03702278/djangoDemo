# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    # return HttpResponse('Hello World!')
    #使用Django的render函数地方,默认找到templates目录下的指定的html文件
    return render(request,"index.html")

#点击登录的按钮后，通过login_action函数来处理请求
def login_action(request):
    #客户端发送的请求信息全部在request，需要获取request里包含的信息
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            #重定向路径，并设置cookie，（cookie名字，cookie内容，cookie在浏览器上保存的时间秒数）
            response = HttpResponseRedirect('/event_manage/')
            response.set_cookie('user',username,3600)
            return response
        else:
            #render函数第三个参数，是字典，显示key对应的value的错误信息.html页面要用{{ error}}，才可以显示对应的内容
            return render(request,'index.html',{'error':'username or password error !'})

def event_manage(request):
    username = request.COOKIES.get('user','')
    return render(request,"event_manage.html",{'user':username})