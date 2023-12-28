import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from posts.models import Post ,Comment
import random
from django.contrib.auth.models import User
from faker import Faker


def add_post(n):
    fake= Faker()
    images=['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']
    for x in range(n):
        Post.objects.create(
            author = User.objects.get(id=random.randint(1,4)),
            title= fake.text(max_nb_chars=10),
            content= fake.text(max_nb_chars=300),
            imag=f"posts/{images[random.randint(0,9)]}",
           

        )
    print(f'{n} posts was created successfully')

#add_post(4)
    

# def add_comment(n):
#     fake = Faker()
#     for x in range(n):
#         Comment.objects.create(
#             author =  User.objects.get(id=random.randint(1,4)),
#             post =  Post.objects.get(id=random.randint(1,6)), 
#             comment =  fake.text(max_nb_chars=300),  
#         )
#     print(f'{n} comments was created successfully')
# add_comment(2)