from django.urls import path
from foodapp import views

urlpatterns = [
   path('home/', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('savedata/', views.savedata, name="savedata"),
    path('display/', views.display, name="display"),
    path('editdata/<int:dataid>', views.editdata, name="editdata"),
    path('deletedata/<int:dataid>', views.deletedata, name="deletedata"),
    path('updatecategory/<int:dataid>', views.updatecategory, name="updatecategory"),
    path('product/', views.product, name="product"),
    path('savepro/', views.savepro, name="savepro"),
    path('displaypro/', views.displaypro, name="displaypro"),
    path('editpro/<int:dataid>', views.editpro, name="editpro"),
    path('updatepro/<int:dataid>', views.updatepro, name="updatepro"),
    path('deletepro/<int:dataid>', views.deletepro, name="deletepro"),
    path('loginn/', views.loginn, name="loginn"),
    path('adminloginn/', views.adminloginn, name="adminloginn"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecontact/<int:dataid>', views.deletecontact, name="deletecontact")
]
