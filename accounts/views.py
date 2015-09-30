from django.shortcuts import render

# Create your views here.
from django.views import generic
#from .models import Post, Comment, PostComment, Reply
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {
        'form': form,
    })