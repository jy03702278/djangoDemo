# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello World!')
    #使用Django的render函数地方,默认找到templates目录下的指定的html文件
    return render(request,"index.html")