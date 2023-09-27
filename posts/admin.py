from django.contrib import admin
from .models import Post , Comment
from django_summernote.admin import SummernoteModelAdmin




class PostAdmin(SummernoteModelAdmin):
    list_display = ['title',"publish_date", "author"]
    summernote_fields = '__all__'




admin.site.register(Post,PostAdmin)
admin.site.register(Comment)