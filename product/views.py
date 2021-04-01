from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
from order.models import ShopCart


def get_product(request):
    return HttpResponse("product page")


def addcomment(request,id):
    url=request.META.get('HTTP_REFERER') # get last url
    if request.method == "POST":         # check post request
        form=CommentForm(request.POST)
        if form.is_valid():
            data=Comment()
            data.subject=form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate=form.cleaned_data['rate']
            data.ip=request.META.get('REMOTE_ADDR')
            data.product_id=id
            current_user=request.user
            data.user_id=current_user.id
            data.save()
            messages.success(request,'your review added successfully')
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)


@login_required(login_url='/login/')
def shopcart(request):
    category=Category.objects.all()
    current_user=request.user
    shop_cart=ShopCart.objects.filter(user_id=current_user.id)


    total=0
    for i in shop_cart:
        total += i.quantity*i.product.price
    context={
        "category":category,
        "cart":shop_cart,
        "total":total,

    }
    return render(request,'shop_cart.html',context)

@login_required(login_url='/login/')
def delete_cart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request,"item delete successfully")


    return HttpResponseRedirect("/product/shopcart/")

def checkout(request):
    return render(request,'checkout.html')


def whilst(request):
    return render(request,'whilst.html')