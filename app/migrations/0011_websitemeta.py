# Generated by Django 5.0.2 on 2024-03-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('about', models.TextField()),
            ],
        ),
    ]
