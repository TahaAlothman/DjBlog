# Generated by Django 4.2 on 2023-08-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imag',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
