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
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    return render(request, "weight_interface/cerealcrops_list.html", {"current_page": current_page})


def get_update_detail_cerealcrop(request, pk):
    cerealcrop = get_object_or_404(CerealCrops, pk=pk)  # нет темплейта
    return render(request, "weight_interface/cerealcrop_detail.html", {"cerealcrop": cerealcrop})


def get_logshippedproducts(request):
    log_shipped_products = LogShippedProducts.objects.all()
    items_per_page = 10
    paginator = Paginator(log_shipped_products, items_per_page)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    return render(request, "weight_interface/log_shipped_products_list.html",
                  {"current_page": current_page})


def get_update_detail_logshippedproducts(request, pk):
    log_shipped_product = get_object_or_404(LogShippedProducts, pk=pk)  # нет темплейта
    return render(request, "weight_interface/log_shipped_product_detail.html",
                  {"log_shipped_product": log_shipped_product})


def get_auxiliarymaterials(request):
    auxiliarymaterials = AuxiliaryMaterials.objects.all()
    items_per_page = 10
    paginator = Paginator(auxiliarymaterials, items_per_page)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    return render(request, "weight_interface/auxiliarymaterials_list.html",
                  {"current_page": current_page})
