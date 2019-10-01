from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .models import Ipost
from django.utils import timezone
from .forms import PostForm
from .forms import IpostForm
from django.contrib.auth.decorators import login_required
"""
order by desc : -published_date
order by asc : published_date
"""
# 기존 post 정보

# def post_list(request):
# 	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
# 	return render(request, 'blog/post_list.html',{'posts': posts})

# def post_detail(request, pk):
# 	post = get_object_or_404(Post, pk=pk)
# 	""" post = Post.objects.get(pk=pk) """
# 	return render(request, 'blog/post_detail.html',{'post': post})

# @login_required
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(request.FILES)
#     return render(request, 'blog/post_edit.html', {'form': form})

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})

# @login_required
# def post_remove(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete()
#     return redirect('post_list')

def post_list(request):
	posts = Ipost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Ipost, pk=pk)
	return render(request, 'blog/post_detail.html',{'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = IpostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = IpostForm(request.FILES)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Ipost, pk=pk)
    if request.method == "POST":
        form = IpostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = IpostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Ipost, pk=pk)
    post.delete()
    return redirect('post_list')
