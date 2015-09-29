from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.core.urlresolvers import reverse
from .models import Post, Comment, PostComment, Reply

class ListPostView(generic.ListView):

	model = Post
	template_name = 'posts/post_list.html'
	fields = ('__all__')

class CreatePostView(generic.CreateView):

	model = Post
	template_name = 'posts/new_post.html'
	fields = ('__all__')

	def get_success_url(self):
		return reverse('post-list')

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(CreatePostView, self).form_valid(form)

class PostView(generic.DetailView):

	model = Post
	template_name = 'posts/post.html'
	fields = ('__all__')

class UpdatePostView(generic.UpdateView):

	model = Post
	template_name = 'posts/post_modify.html'
	fields = ('__all__')

	def get_absolute_url(self):
		return reverse('posts/post-detail', kwargs={'pk': self.pk})

class DeletePostView(generic.DeleteView):

	model = Post
	template_name = 'posts/delete_post.html'

	def get_success_url(self):
		return reverse('post-list')

class CommentListView(generic.ListView):

	model = PostComment 
	template_name = 'posts/post.html'

class CreateCommentView(generic.CreateView):

	model = Comment
	template_name = 'posts/post.html'
	fields = ('__all__')
	
	def get_success_url(self):
		return reverse('post-list')
		
