from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Ipost, Comment
from django.utils import timezone
from .forms import PostForm, IpostForm, CommentForm
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
        form = IpostForm(request.POST, request.FILES) #파일 처리를 위해 request.FILES 추가
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



def add_comment_to_post(request, pk):
    post = get_object_or_404(Ipost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
