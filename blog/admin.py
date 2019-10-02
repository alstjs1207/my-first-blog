from django.contrib import admin
from .models import Post, Ipost, Comment

#admin 관리
#admin.site.register(Post)
admin.site.register(Ipost)
admin.site.register(Comment)
