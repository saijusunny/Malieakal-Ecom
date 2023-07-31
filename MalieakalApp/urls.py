from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    #############################################################<<<<<<<<< LANDING MODULE >>>>>>>>>>>>>>>>>
    path('', views.index, name='index'),
    path('user_type', views.user_type, name='user_type'),
    path('login_main',views.login_main, name='login_main'),
    path('forgotPassword/', views.forgotPassword,name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate,name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword,name='resetPassword'),
    path('logout/', views.logout,name='logout'),

    ############################################################ <<<<<<<<< Staff MODULE >>>>>>>>>>>>>>>>>
 
    path('staff_home/',views.staff_home,name='staff_home'),

    ############################################################ <<<<<<<<< User MODULE >>>>>>>>>>>>>>>>>

    path('user_registration/',views.user_registration,name='user_registration'),
    path('index_user_confirmation/<int:user_id>/',views.index_user_confirmation,name='index_user_confirmation'),
    path('profile_user_creation/',views.profile_user_creation,name='profile_user_creation'),
    path('user_home/',views.user_home,name='user_home'),
    path('category_items/<int:category>',views.category_items,name='category_items'),#--- Category item view template
    path('add_cart/<int:id>/<int:category>',views.add_cart,name='add_cart'),
    path('cart_view',views.cart_view,name='cart_view'),#-----------------------------Cart View Template
    path('cart_checkout',views.cart_checkout,name='cart_checkout'),
    path('send_receipt',views.send_receipt,name='send_receipt'),
    ]