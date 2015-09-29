# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name=b'date modified')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name=b'date modified')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'post published')),
                ('comment', models.ForeignKey(to='posts.Comment')),
                ('post', models.ForeignKey(to='posts.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date posted')),
                ('comment', models.ForeignKey(related_name='replies', to='posts.Comment')),
                ('reply', models.ForeignKey(related_name='parent_comments', to='posts.Comment')),
            ],
        ),
    ]
