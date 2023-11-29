from django.urls import path

from . import views
from .views import *
urlpatterns = [
    path('', views.home, name="home"),

    path('cerealcrops_list/', views.get_cerealcrops, name="cerealcrops"),
    path('cerealcrop/get_update/<int:pk>/', views.get_update_detail_cerealcrop, name="cerealcrops_detail"),
    path('cerealcrop/delete/<int:pk>/', views.delete_cerealcrop, name="delete_cerealcrop"),
    path('create_cerealcrop/', views.post_cerealcrop, name="create_cerealcrop"),

    path('log_shipped_products_list/', views.get_logshippedproducts, name="log_shipped_products"),
    path('create_log_shipped_products/', views.post_logshippedproduct, name="create_log_shipped_product"),
    path('logshippedproduct/get_update/<int:pk>/', views.get_update_detail_logshippedproduct,
         name="logshippedproduct_detail"),
    path('logshippedproduct/delete/<int:pk>/', views.delete_logshippedproduct, name="delete_logshippedproduct"),

    path('auxiliarymaterials_list/', views.get_auxiliarymaterials, name="auxiliarymaterials"),
    path('auxiliarymaterial_post/', views.post_auxiliarymaterial, name="create_auxiliarymaterial"),
    path('auxiliarymaterial/get_update/<int:pk>/', views.get_update_detail_auxiliarymaterial,
         name="auxiliarymaterial_detail"),
    path('auxiliarymaterial/delete/<int:pk>/', views.delete_auxiliarymaterial, name="delete_auxiliarymaterial"),
]