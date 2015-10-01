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


from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView

from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

urlpatterns = patterns(" ", 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, {'template_name': 'posts/login.html'}, name="login"),
    url(r'^logout/$', auth_views.logout, {'template_name': 'posts/logged_out.html'}, name="logout"),
    url(r'^register/$', posts.views.register, name="register"),
    url(r'^blog/$', login_required(posts.views.ListPostView.as_view()), name="post-list"),
    url(r'^blog/(?P<pk>\d+)/$', login_required(posts.views.PostView.as_view()), name="post-detail"),
    url(r'^blog/new/$', login_required(posts.views.CreatePostView.as_view()), name="post-new"),
    url(r'^blog/(?P<pk>\d+)/modify/$', login_required(posts.views.UpdatePostView.as_view()), name="post-modify"),
    url(r'^blog/(?P<pk>\d+)/delete/$', login_required(posts.views.DeletePostView.as_view()), name="post-delete"),
    url(r'^blog/(?P<post_id>[0-9]+)/comments/$', posts.views.addComment, name="postComment"),
    url(r'^comments(?P<comment_id>[0-9]+)/reply/$', posts.views.addComment, name="reply"),
    url(r'^comments(?P<comment_id>[0-9]+)/modifycomment/$', posts.views.modifyComment, name="modifyComment"),
    url(r'^comments(?P<comment_id>[0-9]+)/deletecomment/$', posts.views.deleteComment, name="deleteComment"),
)


urlpatterns += staticfiles_urlpatterns()