# Generated by Django 5.0.2 on 2024-03-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default='False'),
            preserve_default=False,
        ),
    ]
