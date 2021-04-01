from django.urls import path
from . import views
urlpatterns = [

    path('order/',views.order,name='order'),
    path('addtocard/<int:id>/',views.addtocard,name='addtocard'),
    path('login/',views.login,name='login'),


]