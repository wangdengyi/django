from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
def home(request):
    return HttpResponse("Hello,Django")


def detail(request,my_args):
    return HttpResponse("You're looking at my_args %s" %my_args)

def db(request,my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" %(post.title, post.category, post.date_time, post.content))
    return HttpResponse(str) 

def test(request):
    return render(request,'template.html',{'current_time':datetime.now()})
