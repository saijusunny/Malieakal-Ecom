from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


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
    ############################################################ <<<<<<<<< admin MODULE >>>>>>>>>>>>>>>>>
      
    path('admin_home/',views.admin_home,name='admin_home'),
    path('admin_delete_item/<int:id>/', views.admin_delete_item, name='admin_delete_item'),

    path('admin_add_item',views.admin_add_item,name='admin_add_item'),
    path('admin_edit_item/<int:item_id>',views.admin_edit_item,name='admin_edit_item'),
    path('upload_images',views.upload_images,name='upload_images'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('admin_itemlist/',views.admin_itemlist,name='admin_itemlist'),
    path('staff_all_list/', views.staff_all_list, name='staff_all_list'),
    path('admin_category/', views.admin_category, name='admin_category'),
    path('new_form/', views.new_form, name='new_form'),
    path('staff_management/', views.staff_management, name='staff_management'), 
    path('edit_staff/<int:id>', views.edit_staff, name='edit_staff'),
    path('delete_staff/<int:id>', views.delete_staff, name='delete_staff'),
    path('edit_banner/<int:id>', views.edit_banner, name='edit_banner'),
    path('product_management/', views.product_management, name='product_management'),  
    path('category_management/', views.category_management, name='category_management'),
    path('ad_category_list/', views.ad_category_list, name='ad_category_list'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('delete_cat/<int:id>', views.delete_cat, name='delete_cat'),
    path('ad_offerlist/', views.ad_offerlist, name='ad_offerlist'),
    path('ad_edit_offer/<int:id>', views.ad_edit_offer, name='ad_edit_offer'),
    path('ad_delete_offer/<int:id>', views.ad_delete_offer, name='ad_delete_offer'),
    path('ad_offer_management/', views.ad_offer_management, name='ad_offer_management'),
    path('ad_view_order/', views.ad_view_order, name='ad_view_order'),
    path('ad_delete_check/<int:id>', views.ad_delete_check, name='ad_delete_check'),

    path('user_list_view', views.user_list_view, name='user_list_view'),
    path('edit_user/<int:id>', views.edit_user, name='edit_user'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'), 
    path('render_user_pdf/<int:id>', views.render_user_pdf, name='render_user_pdf'),
    path('export_user_excel/', views.export_user_excel, name='export_user_excel'),
    path('admin_subcategory/', views.admin_subcategory, name='admin_subcategory'),
    path('edit_subcategory/<int:id>', views.edit_subcategory, name='edit_subcategory'),
    path('ad_save_new_arrival/', views.ad_save_new_arrival, name='ad_save_new_arrival'),
    path('ad_edit_newarrival/<int:id>', views.ad_edit_newarrival, name='ad_edit_newarrival'),
    path('ad_delete_newarrival/<int:id>', views.ad_delete_newarrival, name='ad_delete_newarrival'),
    path('ad_newarrival/', views.ad_newarrival, name='ad_newarrival'),
    path('ad_newarrival_management/', views.ad_newarrival_management, name='ad_newarrival_management'),
    ############################################################ <<<<<<<<< Staff MODULE >>>>>>>>>>>>>>>>>
  
    
    path('staff_home/',views.staff_home,name='staff_home'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('profile_staff_creation/',views.profile_staff_creation,name='profile_staff_creation'),
    
    path('new_module',views.new_module,name='new_module'), # staff item add
    path('staff_itemlist',views.staff_itemlist,name='staff_itemlist'), # view list 
    path('staff_itemedit/<int:item_id>',views.staff_itemedit,name='staff_itemedit'),
    path('staff_itemdelete/<int:item_id>',views.staff_itemdelete,name='staff_itemdelete'), 
 

     

    path('staff_upload_images',views.staff_upload_images,name='staff_upload_images'),

    path('staff_new_offer/', views.staff_new_offer, name='staff_new_offer'),
    path('staffofferlist/', views.staffofferlist, name='staffofferlist'),
    path('edit_offer/<int:id>', views.edit_offer, name='edit_offer'),
    path('delete_offer/<int:id>', views.delete_offer, name='delete_offer'),
    
    path('staff_category',views.staff_category,name='staff_category'),
    path('staff_categorylist',views.staff_categorylist,name='staff_categorylist'),
    path('edit_staffcateg/<int:id>', views.edit_staffcateg, name='edit_staffcateg'),
    path('delete_staffcateg/<int:id>', views.delete_staffcateg, name='delete_staffcateg'),

    path('staff_view_order',views.staff_view_order,name='staff_view_order'),
    path('staff_delete_check/<int:id>', views.staff_delete_check, name='staff_delete_check'),

    path('staff_user_list_view',views.staff_user_list_view,name='staff_user_list_view'),
    path('staff_edit_user/<int:id>', views.staff_edit_user, name='staff_edit_user'),
    path('staff_delete_user/<int:id>', views.staff_delete_user, name='staff_delete_user'),


    path('staff_edit_banner/<int:id>', views.staff_edit_banner, name='staff_edit_banner'),
    path('staff_subcategory', views.staff_subcategory, name='staff_subcategory'),
    path('staff_edit_subcategory/<int:id>', views.staff_edit_subcategory, name='staff_edit_subcategory'),
    
    ############################################################ <<<<<<<<< User MODULE >>>>>>>>>>>>>>>>>

    path('user_registration/',views.user_registration,name='user_registration'),
    path('index_user_confirmation/<int:user_id>/',views.index_user_confirmation,name='index_user_confirmation'),
    path('profile_user_creation/',views.profile_user_creation,name='profile_user_creation'),
    path('user_home/',views.user_home,name='user_home'),
    path('all_items/',views.all_items,name='all_items'),
    path('all_items_add_cart/<int:id>/<int:category>',views.all_items_add_cart,name='all_items_add_cart'),

    path('index_user_confirmation/<int:user_id>/',views.index_user_confirmation,name='index_user_confirmation'),
    path('category_items/<int:categorys>',views.category_items,name='category_items'),#--- Category item view template 
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
    path('ind',views.ind,name='ind'),


    path('search_feature',views.search_feature,name='search_feature'),
    path('index_search_feature',views.index_search_feature,name='index_search_feature'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('edit_user_profile/<int:id>',views.edit_user_profile,name='edit_user_profile'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)