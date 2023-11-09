from django.contrib import admin
from social.models import Post



# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

