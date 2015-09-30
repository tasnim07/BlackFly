from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
# Create your views here.
from django.views import generic
from django.core.urlresolvers import reverse
from .models import Post, Comment, PostComment, Reply

class ListPostView(generic.ListView):

	model = Post
	template_name = 'posts/post_list.html'
	context_object_name = 'latest_blog_posts'

	def get_queryset(self):
		return Post.objects.order_by('-pub_date')

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

def addComment(request, post_id=None, comment_id=None):
	
	next = getNextUrl(request)
	
	if (request.method != 'POST'):
		raise Http404();

	new_comment = Comment.objects.create(body=request.POST['body'])
	
	if (post_id):
		# add comment to post
		post = get_object_or_404(Post, pk=post_id)
		PostComment.objects.create(post=post, comment=new_comment)

	elif (comment_id):
		# add reply to comment
		comment = get_object_or_404(Comment, pk=comment_id)
		Reply.objects.create(comment=comment, reply=new_comment)
	return redirect(next)

def modifyComment(request, comment_id):
	next = getNextUrl(request)
	comment = get_object_or_404(Comment, pk=comment_id)
	comment.body = request.POST['body']
	comment.save()
	return redirect(next)

def deleteComment(request, comment_id):
	next = getNextUrl(request)
	comment = get_object_or_404(Comment, pk=comment_id)
	comment.delete()
	return redirect(next)

def getNextUrl(request):
	''' Gets the url specified by 'next' GET parameter; uses default otherwise '''
	try:
		next = request.GET['next']
	except KeyError:
		return reverse('post-list')
	return next;
