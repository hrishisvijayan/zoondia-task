
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('seller-signup/',views.signup,name='seller-signup'),
    path('addproduct/',views.create_product,name='addproduct'),
    path('viewproducts/',views.view_products,name='viewproducts'),
    path('editproduct/<int:id>',views.edit_product,name='editproduct'),
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path('viewcart',views.cartpage,name='viewcart'),
]