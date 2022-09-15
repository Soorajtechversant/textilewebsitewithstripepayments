
from re import template
from django.urls import path, include
from membership.views import *
from .views import *
from membership import views


urlpatterns = [
    path('',Customer_index.as_view(),name="products/customer/customer_index" ),
    # path('settings',views.settings,name='settings'), 
    path('registration',Registration.as_view(),name="products/registration/registration"),
    # path('auth/login/', views.Login.as_view(), name='Login'),
    path('auth/login/',Login.as_view(),name="products/registration/login"),

    path('owner_index/',Owner_index.as_view(),name="products/productshop_owner/owner_index"),
    path('add_product/',Add_product.as_view(),name="products/productshop_owner/add_product"),
    path('edit_product/<int:id>/',Edit_product.as_view(),name="products/productshop_owner/edit_product"),
    path('Delete_product/<int:id>',Delete_product.as_view(),name="products/productshop_owner/Delete_product"),
   
    path('customer_index/',Customer_index.as_view(),name="products/customer/customer_index"),
    
    path('book_product/',Book_product.as_view(),name="products/customer/book_product"),

    # path('auth/login/', views.Login.as_view(), name='Login'),
    path('api/checkout-session/<id>/', create_checkout_session, name='api_checkout_session'),
    path('detail/<id>/', productDetailView.as_view(), name='detail'),
    # path('success/', PaymentSuccessView.as_view(), name='success'),
    path('cancel/', PaymentFailedView.as_view(), name='cancel'),


    path('subscription',views.subscription,name='subscription'), 
    path('premium',views.premium,name='premium'), 
    # path('auth/', include('django.contrib.auth.urls')),
    # path('auth/signup', views.SignUp.as_view(), name='signup'),
    # path('auth/login/', views.Login.as_view(), name='Login'),
    path('auth/settings', views.settings, name='settings'),



    path('updateaccounts', views.updateaccounts, name='updateaccounts'),
    path('deletesub',views.delete,name='delete'),
    path('modify',views.modify,name='modify'), 
    path('pause',views.pausepayments,name='pausepayments'),
    path('unpause',views.unpause,name='unpause'),
    path('success', views.success, name='success'),
    path('downgrade',views.downgrade,name='downgrade'),

    path('logout/',Logout.as_view(),name="logout"),



]