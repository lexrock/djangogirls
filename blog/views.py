from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404
from .froms import PostForms
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForms()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForms(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForms(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})
