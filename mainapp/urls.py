from django.urls import path
from mainapp import views


urlpatterns =[
    path('homepage/',views.homepage,name="homepage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('shoppage/<products>/',views.shoppage,name="shoppage"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('checkpage/', views.checkpage, name="checkpage"),
    path('singlepage/<int:dataid>/', views.singlepage, name="singlepage"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('savecart/', views.savecart, name="savecart"),
    path('deletecart/<int:dataid>/', views.deletecart, name="deletecart"),
    path('savecheckout/', views.savecheckout, name="savecheckout"),
    path('userpage/', views.userpage, name="userpage"),
    path('usersavedata/', views.usersavedata, name="usersavedata"),
    path('userloginpage/', views.userloginpage, name="userloginpage"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('gateway/', views.gateway, name="gateway"),


]