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
    path('all_items/',views.all_items,name='all_items'),
    path('all_items_add_cart/<int:id>/<int:category>',views.all_items_add_cart,name='all_items_add_cart'),

    path('index_user_confirmation/<int:user_id>/',views.index_user_confirmation,name='index_user_confirmation'),
    path('category_items/<int:category>',views.category_items,name='category_items'),#--- Category item view template 
    path('under_category_items_add_cart/<int:id>/<int:categorys>',views.under_category_items_add_cart,name='under_category_items_add_cart'),

    path('under_items/<str:category>',views.under_items,name='under_items'),
    path('add_cart_pr_view/<int:id>/<int:category>',views.add_cart_pr_view,name='add_cart_pr_view'),

    path('add_cart/<int:id>/<int:category>',views.add_cart,name='add_cart'),
    path('add_cart_pr_view/<int:id>/<int:category>',views.add_cart_pr_view,name='add_cart_pr_view'),
    path('cart_view',views.cart_view,name='cart_view'),
    path('home',views.home,name='home'),#-----------------------------Cart View Template
    path('cart_checkout',views.cart_checkout,name='cart_checkout'),
    path('send_receipt',views.send_receipt,name='send_receipt'),
    path('product_view/<int:item_id>/', views.product_view, name='product_view'),
    path('delete_cart/<int:id>',views.delete_cart,name='delete_cart'),
    
    ]