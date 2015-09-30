"""BlackFly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
import posts.views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(" ", 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', posts.views.ListPostView.as_view(), name="post-list"),
    url(r'^blog/(?P<pk>\d+)/$', posts.views.PostView.as_view(), name="post-detail"),
    url(r'^blog/new/$', posts.views.CreatePostView.as_view(), name="post-new"),
    url(r'^blog/(?P<pk>\d+)/modify/$', posts.views.UpdatePostView.as_view(), name="post-modify"),
    url(r'^blog/(?P<pk>\d+)/delete/$', posts.views.DeletePostView.as_view(), name="post-delete"),
    url(r'^blog/(?P<post_id>[0-9]+)/comments/$', posts.views.addComment, name="postComment"),
    url(r'^comments(?P<comment_id>[0-9]+)/reply/$', posts.views.addComment, name="reply"),
    url(r'^comments(?P<comment_id>[0-9]+)/modifycomment/$', posts.views.modifyComment, name="modifyComment"),
    url(r'^comments(?P<comment_id>[0-9]+)/deletecomment/$', posts.views.deleteComment, name="deleteComment"),
)


urlpatterns += staticfiles_urlpatterns()