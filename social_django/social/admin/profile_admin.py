from django.contrib import admin
from social.models import Profile



# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


