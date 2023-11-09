from django.contrib import admin
from social.models import Tag



# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

