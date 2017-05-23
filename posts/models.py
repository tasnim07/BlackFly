from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    modified_date = models.DateTimeField('date modified', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.id})


class Comment(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    modified_date = models.DateTimeField('date modified', auto_now=True)

    def __str__(self):
        return self.body


class PostComment(models.Model):
    post = models.ForeignKey(Post)
    comment = models.ForeignKey(Comment)
    pub_date = models.DateTimeField('post published', auto_now_add=True)


class Reply(models.Model):
    reply = models.ForeignKey(Comment, related_name='parent_comments')
    comment = models.ForeignKey(Comment, related_name='replies')
    pub_date = models.DateTimeField('date posted', auto_now_add=True)
