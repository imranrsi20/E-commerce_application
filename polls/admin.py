from django.contrib import admin

# Register your models here.
from polls.models import *
# Register your models here.py
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company','status']
    list_filter = ['status']

admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactMessage)