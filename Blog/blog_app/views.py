from django.shortcuts import render
from django.http import HttpResponse
from blog_app.models import Article
from datetime import datetime
from django.http import Http404

def home(request):
    post_list = Article.objects.all()  # get all article objects
    return render(request, 'blog/home.html', {'post_list': post_list})

def resume(request):
    return render(request, 'blog/resume.html')

def Test(request):
    return render(request, 'blog/test.html', {'current_time': datetime.now()})

def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'blog/post.html',{'post':post})
