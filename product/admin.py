from django.contrib import admin

from product.models import *
# Register your models here.py
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','status']
    list_filter = ['status']

class ProductyAdmin(admin.ModelAdmin):
    list_display = ['title','category','status']
    list_filter = ['category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductyAdmin)