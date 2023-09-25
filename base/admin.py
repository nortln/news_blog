from django.contrib import admin

from .models import Comment, New

admin.site.register(Comment)
admin.site.register(New)