"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/remove/<int:pk>/', views.post_remove, name='post_remove'),
    path('post/comment/<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/approve/<int:pk>/', views.comment_approve, name='comment_approve'),
    path('comment/remove/<int:pk>/', views.comment_remove, name='comment_remove'),
]
