from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.forms import ModelForm, TextInput


class Setting(models.Model):
    STATUS=(
        ('TRUE','TRUE'),
        ('FALSE','FALSE'),
    )
    title=models.CharField(max_length=150)
    keywords=models.CharField(max_length=250)
    description=models.CharField(max_length=255)
    company=models.CharField(max_length=70)
    address=models.CharField(blank=True,max_length=150)
    phone=models.CharField(blank=True,max_length=15)
    fax=models.CharField(blank=True,max_length=15)
    email=models.CharField(blank=True,max_length=50)
    smtpserver=models.CharField(blank=True,max_length=50)
    smtpemail=models.CharField(blank=True,max_length=50)
    smtppassword=models.CharField(blank=True,max_length=10)
    smtpport=models.CharField(blank=True,max_length=5)
    icon=models.ImageField(blank=True,upload_to='media_images/')
    facebook=models.CharField(blank=True,max_length=50)
    instagram=models.CharField(blank=True,max_length=50)
    twitter=models.CharField(blank=True,max_length=50)
    youtube=models.CharField(blank=True,max_length=50)
    aboutus=RichTextUploadingField(blank=True)
    contact=RichTextUploadingField(blank=True)
    references=RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title




class ContactMessage(models.Model):
    STATUS=(
        ('NEW','NEW'),
        ('READ','READ'),
        ('CLOSED','CLOSED'),
    )
    name=models.CharField(blank=True,max_length=50)
    email=models.CharField(blank=True,max_length=70)
    subject=models.CharField(blank=True,max_length=100)
    message=models.TextField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='NEW')
    ip=models.CharField(blank=True,max_length=20)
    note=models.CharField(blank=True,max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name



class ContactForm(ModelForm):
    class Meta:
        model=ContactMessage
        fields=['name','email','subject','message']
        widgets={

            'name' : TextInput(attrs={'class': 'input','placeholder':'Name'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Message','rows':'5'}),
        }

