from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
# Create your views here.
from django.views import generic
from django.core.urlresolvers import reverse
from .models import Post, Comment, PostComment, Reply
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

class PostOwnerMixin(object):

	def get_object(self, queryset=None):
		""" Returns the object the view is displaying.
		"""
		if queryset is None:
			queryset = self.get_queryset()

		pk = self.kwargs.get(self.pk_url_kwarg, None)
		queryset = queryset.filter(pk=pk, author=self.request.user,)

		try:
			obj = queryset.get()
		except ObjectDoesNotExist:
			raise PermissionDenied

		return obj

class ListPostView(generic.ListView):

	model = Post
	template_name = 'posts/post_list.html'
	context_object_name = 'latest_blog_posts'

	def get_queryset(self):
		return Post.objects.order_by('-pub_date')

class CreatePostView(generic.CreateView):

	model = Post
	template_name = 'posts/new_post.html'
	fields = ('title', 'body')

	def get_success_url(self):
		return reverse('post-list')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(CreatePostView, self).form_valid(form)

class PostView(generic.DetailView):

	model = Post
	template_name = 'posts/post.html'
	fields = ('__all__')

class UpdatePostView(PostOwnerMixin, generic.UpdateView):

	model = Post
	template_name = 'posts/post_modify.html'
	fields = ('title', 'body')

	def get_absolute_url(self):
		return reverse('posts/post-detail', kwargs={'pk': self.pk})

class DeletePostView(PostOwnerMixin, generic.DeleteView):

	model = Post
	template_name = 'posts/delete_post.html'

	def get_success_url(self):
		return reverse('post-list')

@login_required
def addComment(request, post_id=None, comment_id=None):
	
	next = getNextUrl(request)
	
	if (request.method != 'POST'):
		raise Http404();

	new_comment = Comment.objects.create(author=request.user, body=request.POST['body'])
	
	if (post_id):
		# add comment to post
		post = get_object_or_404(Post, pk=post_id)
		PostComment.objects.create(post=post, comment=new_comment)

	elif (comment_id):
		# add reply to comment
		comment = get_object_or_404(Comment, pk=comment_id)
		Reply.objects.create(comment=comment, reply=new_comment)
	return redirect(next)

@login_required
def modifyComment(request, comment_id):
	next = getNextUrl(request)
	comment = get_object_or_404(Comment, pk=comment_id)
	checkAuthor(request, comment)
	comment.body = request.POST['body']
	comment.save()
	return redirect(next)

@login_required
def deleteComment(request, comment_id):
	next = getNextUrl(request)
	comment = get_object_or_404(Comment, pk=comment_id)
	checkAuthor(request, comment)
	comment.delete()
	return redirect(next)

def checkAuthor(request, obj):
	if(request.user.id != obj.author.id):
		raise Http404('You are not authorized to perform this act')

def getNextUrl(request):
	''' Gets the url specified by 'next' GET parameter; uses default otherwise '''
	try:
		next = request.GET['next']
	except KeyError:
		return reverse('post-list')
	return next;

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render(request, "posts/register.html", {
        'form': form,
    })
