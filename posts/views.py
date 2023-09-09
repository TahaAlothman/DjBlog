from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list (request):
    data=Post.objects.all()           #list
    return render(request,'all_posts.html',{'posts':data})





def post_detail (request,post_id):
    data=Post.objects.get(id=post_id)
    return render(request,'post_detail.html',{'post':data})
    



def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form= PostForm()
    return render(request,'add.html',{'form':form})