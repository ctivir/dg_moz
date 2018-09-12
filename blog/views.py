from django.shortcuts import render, get_object_or_404

from blog.forms import PostForm
from blog.models import Post


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})