# Generated by Django 3.2.7 on 2021-09-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]
