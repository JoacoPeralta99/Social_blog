from django.contrib import admin
from social.models import Category



# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

