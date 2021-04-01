from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

from django.utils.safestring import mark_safe
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    STATUS=(
        ('TRUE','TRUE'),
        ('FALSE','FALSE'),
    )
    parent=models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='media_images/')
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField(null=False,unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title






class Product(models.Model):
    STATUS=(
        ('TRUE','TRUE'),
        ('FALSE','FALSE'),
    )
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='media_images/')
    price=models.FloatField()
    amount=models.IntegerField()
    minamount = models.IntegerField()
    detail=RichTextUploadingField()
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField(null=False,unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=True)
    image=models.ImageField(blank=True,upload_to='media_images/')

    def __str__(self):
        return self.title




class Comment(models.Model):
    STATUS=(
        ('NEW','NEW'),
        ('TRUE','TRUE'),
        ('FALSE','FALSE'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50,blank=True)
    comment = models.CharField(max_length=250, blank=True)
    rate=models.IntegerField(default=1)
    status=models.CharField(max_length=10,choices=STATUS,default='NEW')
    ip=models.CharField(max_length=20,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['subject','comment','rate']