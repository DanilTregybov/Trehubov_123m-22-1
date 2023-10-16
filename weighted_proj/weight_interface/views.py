from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import CerealCrops, LogShippedProducts, AuxiliaryMaterials


# Create your views here.
def home(request):
    return render(request, "weight_interface/base.html")


def get_cerealcrops(request):
    cerealcrops = CerealCrops.objects.all()
    items_per_page = 10  # Кількість записів на кожній сторінці
    paginator = Paginator(cerealcrops, items_per_page)
    return render(request, "weight_interface/cerealcrops_list.html", {"cerealcrops": cerealcrops})


def get_update_detail_cerealcrop(request, pk):
    cerealcrop = get_object_or_404(CerealCrops, pk=pk)  # нет темплейта
    return render(request, "weight_interface/cerealcrop_detail.html", {"cerealcrop": cerealcrop})


def get_logshippedproducts(request):
    log_shipped_products = LogShippedProducts.objects.all()
    return render(request, "weight_interface/log_shipped_products_list.html",
                  {"log_shipped_products": log_shipped_products})


def get_update_detail_logshippedproducts(request, pk):
    log_shipped_product = get_object_or_404(LogShippedProducts, pk=pk)  # нет темплейта
    return render(request, "weight_interface/log_shipped_product_detail.html",
                  {"log_shipped_product": log_shipped_product})


def get_auxiliarymaterials(request):
    auxiliarymaterials = AuxiliaryMaterials.objects.all()
    return render(request, "weight_interface/auxiliarymaterials_list.html",
                  {"auxiliarymaterials": auxiliarymaterials})
