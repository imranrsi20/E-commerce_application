from django.shortcuts import render,HttpResponse

# Create your views here.
def get_product(request):
    return HttpResponse("product page")