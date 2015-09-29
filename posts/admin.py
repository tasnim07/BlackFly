from django.contrib import admin

# Register your models here.
from .models import Post, Comment, PostComment, Reply


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostComment)
admin.site.register(Reply)