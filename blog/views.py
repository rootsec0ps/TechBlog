from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "index.html"

#class PostDetailView(DetailView):
#    model = Post
#    template_name = "post_detail.html"

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.order_by('-date_added')
    context = {'post': post, 'comments': comments}
    return render(request, 'post_detail.html', context)

def new_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.order_by('-date_added')

    if request.method != 'POST':
        # When no data is submitted, create a blank form
        form = CommentForm()

    else:
        # POST data submitted, process data
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('blog:post_detail', post_id=post_id)
    
    # Display a blank or invalid form
    context = {'form': form, 'post': post, 'comments': comments}
    return render(request, 'new_comment.html', context)
