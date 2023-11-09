from django.contrib import admin
from social.models import Comment



# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment

