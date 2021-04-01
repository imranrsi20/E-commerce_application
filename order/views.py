from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from order.models import ShopCart, ShopCartForm
from product.models import *


def order(request):
    return HttpResponse("order page")



@login_required(login_url='/login/')
def addtocard(request,id):
    url=request.META.get('HTTP_REFERER') # get last url
    current_user=request.user   # check user
    check_product=ShopCart.objects.filter(product_id=id)  # check same product
    if check_product:
        control = 1      # the product is in the cart
    else:
        control = 0       # the product is not in the cart

    if request.method == "POST":         # check post request
        form=ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:  #then update cart
                data=ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
                total_item = ShopCart.objects.filter(user_id=current_user.id)
                request.session['total_item'] = total_item.count()
            else:  # insert item into shop cart
                data=ShopCart()
                data.user_id=current_user.id
                data.product_id=id
                data.quantity= form.cleaned_data['quantity']
                data.save()
                total_item = ShopCart.objects.filter(user_id=current_user.id)
                request.session['total_item'] = total_item.count()

        messages.success(request,'your item is added in cart')
        return HttpResponseRedirect(url)

    else:  # if there is no post request
        if control == 1:  # then update cart
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
            total_item = ShopCart.objects.filter(user_id=current_user.id)
            request.session['total_item'] = total_item.count()
        else:  # insert item into shop cart
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
            total_item = ShopCart.objects.filter(user_id=current_user.id)
            request.session['total_item'] = total_item.count()

        messages.success(request,'item added succesfully')
        return HttpResponseRedirect(url)
