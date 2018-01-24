from django.shortcuts import render

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
    data = Blog.objects.get(pk=id)
    dictionary = {"data": data}
    return render(request, 'detail.html', dictionary)
