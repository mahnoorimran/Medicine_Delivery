from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name','email','username','location','short_intro','bio','profile_image','Created','id')
admin.site.register(Profile,ProfileAdmin)

