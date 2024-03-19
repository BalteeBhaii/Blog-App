# Generated by Django 5.0.2 on 2024-03-01 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parents',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='replies', to='app.comments'),
        ),
    ]