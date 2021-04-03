from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.utils.crypto import get_random_string
from .models import *
from product.models import *
from user.models import *


from order.models import OrderForm


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


def orderproduct(request):
    category=Category.objects.all()
    current_user=request.user
    shopcart=ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in shopcart:
        total += rs.product.price * rs.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # check bank or credit card information and if everything ok or return error message before save order
            #......code
            data=Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(6).upper()
            data.code = ordercode
            data.save()

            # move shopcart items to order product items

            shopcart=ShopCart.objects.filter(user_id=current_user.id)
            for rs in shopcart:
                detail=OrderProduct()
                detail.order_id = data.id # order id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()

                # reduce quantity of sold product from amount of product

                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()

                #********<>**********

            ShopCart.objects.filter(user_id=current_user.id).delete()  # clear and delete shopcart
            request.session['total_item'] = 0
            messages.success(request,'your order has been completed.thank you')
            return render(request,'order_completed.html',{'ordercode':ordercode,'category':category})
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/orderproduct')
    form = OrderForm()
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    profile = UserProfile.objects.get(user_id=current_user.id)
    context={
        'shopcart':shopcart,
        'category':category,
        'total':total,
        'form':form,
        'profile':profile,
    }


    return render(request,'checkout.html',context)