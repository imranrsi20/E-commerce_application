from django.contrib import admin

from product.models import *
# Register your models here.py
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','status']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']

class ProductyAdmin(admin.ModelAdmin):
    list_display = ['title','category','status','image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductyAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment)