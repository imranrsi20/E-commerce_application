from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
import json

# Create your views here.
from polls.models import *

from .models import ContactForm, ContactMessage
from product.models import *



def index(request):
    setting=Setting.objects.get(pk=1)
    slider_product=Product.objects.all().order_by('id')[:4] # first 4 product
    latest_product=Product.objects.all().order_by('-id')[:4] # last 4 product
    pick_product = Product.objects.all().order_by('?')[:4]  # random 4 product



    context={
        "setting":setting,
        "s_p":slider_product,
        "l_p":latest_product,
        "p_p":pick_product,
    }

    return render(request,'index.html',context)

def about(request):
    setting = Setting.objects.get(pk=1)
    context = {
        "setting": setting,
    }

    return render(request, 'about.html', context)

def contact(request):
    setting = Setting.objects.get(pk=1)

    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()   #relation with model
            data.name=form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'your message has been sent,thank you for your interest')  # flash message
            return HttpResponseRedirect('/contact/')
    form=ContactForm
    context = {
        "setting": setting,
        "form":form,
    }

    return render(request, 'contact.html', context)


def product_detail(request,id,slug):
    category=Category.objects.all()
    product=Product.objects.get(pk=id)
    images=Images.objects.filter(product__id=id)
    comments=Comment.objects.filter(product__id=id)
    t_comment=comments.count()
    n_p=images.count()

    context={
        "category":category,
        "product":product,
        "images":images,
        "comments":comments,
        "t_comment":t_comment,
        "n_p":n_p,
    }

    return render(request,'product_detail.html',context)

def addtocard(request,id):
    return HttpResponse("this is card")

def Search(request):
    if request.method == 'POST':
        key=request.POST['search']
        product=Product.objects.filter(title__icontains=key)

        context={
            's_p':product,
        }
    return render(request,'search.html',context)


def search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    product = Product.objects.filter(title__icontains=q)
    results = []
    for p in product:
      product_json = {}
      product_json = p.title
      results.append(product_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)


