# Generated by Django 5.0.2 on 2024-03-03 08:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_post_bookmarks'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, default='None', related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]
