from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('cerealcrops/', views.get_cerealcrops, name="cerealcrops"),
    path('cerealcrops/get_update/<int:pk>/', views.get_update_detail_cerealcrop, name="theme_detail"),
]