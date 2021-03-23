from django.db import models

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
    slug=models.SlugField()
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
    detail=models.TextField()
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title,self.amount



