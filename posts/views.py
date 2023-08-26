from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list (request):
    data=Post.objects.all()           #list
    return render(request,'all_posts.html',{'posts':data})





def post_detail (request):
    pass