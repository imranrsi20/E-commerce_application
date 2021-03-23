from django.shortcuts import render,HttpResponse

# Create your views here.

def get_polls(request):
    return render(request,'index.html')