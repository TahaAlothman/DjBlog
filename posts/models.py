from django.db import models

'''
    - html widget
    - validation
    - best for db

'''

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=5000)
    publish_date = models.DateTimeField()