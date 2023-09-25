from django.views import generic
from .models import Post


'''
templates:post_list.html
context: post_list, object_list
'''


class Postlist(generic.ListView):
    model = Post

'''
templates:post_detail.html
context: post, object
'''


class Postdetail(generic.DetailView):
    model = Post


'''
templates:post_form.html
'''

class Postcreate(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url='/blog/'