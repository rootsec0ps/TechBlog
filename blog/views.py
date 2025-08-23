from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Reply
from .forms import ReplyForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

#class PostDetailView(DetailView):
#    model = Post
#    template_name = "post_detail.html"

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    replies = post.reply_set.order_by('-date_added')
    context = {'post': post, 'replies': replies}
    return render(request, 'post_detail.html', context)

def new_reply(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    replies = post.reply_set.order_by('-date_added')

    if request.method != 'POST':
        # When no data is submitted, create a blank form
        form = ReplyForm()

    else:
        # POST data submitted, process data
        form = ReplyForm(data=request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.post = post
            new_reply.save()
            return redirect('blog:post_detail', post_id=post_id)
    
    # Display a blank or invalid form
    context = {'form': form, 'post': post, 'replies': replies}
    return render(request, 'new_reply.html', context)
