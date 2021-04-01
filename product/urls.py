from django.urls import path
from . import views
urlpatterns = [

    path('',views.get_product,name='product'),
    path('addcomment/<int:id>/',views.addcomment,name='addcomment'),
    path('shopcart/',views.shopcart,name='shopcart'),
    path('checkout/',views.checkout,name='checkout'),
    path('whilst/',views.whilst,name='whilst'),
    path('delete_cart/<int:id>/',views.delete_cart,name='delete_cart'),


]