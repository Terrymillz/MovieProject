# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0010_delete_movie'),
        ('movieApp', '0002_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_Movie_code', models.CharField(max_length=100)),
                ('movie_title', models.CharField(max_length=50)),
                ('poster_path', models.CharField(max_length=100)),
                ('backdrop_path', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=140)),
                ('score', models.PositiveIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='User_app.User')),
            ],
        ),
    ]