from __future__ import unicode_literals
from sqlDemo import models
from django.shortcuts import render
from django.shortcuts import HttpResponse

# 展示数据库内容
def list(request):
    people_list = models.message.objects.all()
    return render("showuser.html", {"data":people_list})
# 插入数据
def insert(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.message.objects.create(username=username, password=password)
        models.message.save()
    return render('insert.html')

# helloworld
def text(request):
    return HttpResponse("hello world")

