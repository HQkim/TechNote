# Generated by Django 3.2.8 on 2021-10-22 07:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='like',
        ),
        migrations.AddField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
