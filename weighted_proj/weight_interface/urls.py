from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('cerealcrops_list/', views.get_cerealcrops, name="cerealcrops"),
    path('cerealcrops/get_update/<int:pk>/', views.get_update_detail_cerealcrop, name="cerealcrops_detail"),

    path('log_shipped_products_list/', views.get_logshippedproducts, name="log_shipped_products"),

    path('auxiliarymaterials_list/', views.get_auxiliarymaterials, name="auxiliarymaterials"),
]