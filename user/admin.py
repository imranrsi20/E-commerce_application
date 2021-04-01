from django.contrib import admin

from user.models import *
# Register your models here.py

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address','phone','city','country','image_tag']
    list_filter = ['user','phone','country']
    readonly_fields = ('image_tag',)

admin.site.register(UserProfile,UserProfileAdmin)
