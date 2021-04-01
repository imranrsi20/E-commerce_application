from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('product/<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    path('card/<int:id>/',views.addtocard,name='card'),
    path('search/',views.Search,name='search'),
    path('search_auto/',views.search_auto,name='search_auto'),



]