from django.views import generic
from .models import Post, Comment


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
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.filter(post = self.get_object())
        return context

'''
templates:post_form.html
'''

class Postcreate(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url='/blog/'



class Postupdate(generic.UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'posts/edit.html/'
    success_url='/blog/'



class Postdelete(generic.DeleteView):
    model = Post
    success_url='/blog/'