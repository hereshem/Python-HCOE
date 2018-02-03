from django.http.response import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Blog
# Create your views here.

def index(request):
    skip = 0
    limit = 10
    data = Blog.objects.order_by("-title")[skip:limit]
    count1 = Blog.objects.count()

    dictionary = {"data" : data, "count" :count1}
    return render(request, 'index.html', dictionary)

def detail(request, id):
    try:
        data = Blog.objects.get(pk=id)
        dictionary = {"data": data}
    except Exception:
        return render(request, "404.html",{})
    return render(request, 'detail.html', dictionary)

def sendJson(request):
    return HttpResponse(serializers.serialize("json", Blog.objects.all()))

def getPostTest(request):
    return HttpResponse(request.GET.lists())
    return HttpResponse(serializers.serialize("json", Blog.objects.all()))