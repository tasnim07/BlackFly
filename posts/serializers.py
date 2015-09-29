from rest_framework import serializers
from posts.models import Post, Comment, PostComment, Reply

class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ('author', 'title', 'body', 'pub_date', 'modified_date')


class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields = ('author', 'body', 'pub_date', 'modified_date')


class PostCommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = PostComment
		fields = ('post', 'comment', 'pub_date')


class ReplySerializer(serializers.ModelSerializer):

	class Meta:
		model = Reply
		fields = ('reply', 'comment', 'pub_date')

