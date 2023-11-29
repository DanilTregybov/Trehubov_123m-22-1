from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from .forms import CerealCropsForm, AuxiliaryMaterialsForm, LogShippedProdForm
from .models import CerealCrops, LogShippedProducts, AuxiliaryMaterials

from datetime import datetime


# def current_datetime(request):
#     current_datetime = datetime.now()
#     return render(request, 'current_datetime.html', {'datetime': current_datetime})
# Create your views here.
@login_required
@csrf_exempt
def home(request):
    return render(request, "weight_interface/base.html")


@login_required
@csrf_exempt
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


@login_required
@csrf_exempt
def post_cerealcrop(request):
    datetime_now = datetime.now().strftime('%Y-%m-%d')
    error = ""
    if request.method == "POST":
        form = CerealCropsForm(request.POST)
        if form.is_valid():
            cerealcrop = form.save(commit=False)
            cerealcrop.save()
            return redirect("cerealcrops")
        else:
            error = "Form don`t valid"
    form = CerealCropsForm()
    context = {
        "form": form,
        "error": error,
        "datetime_now": datetime_now
    }
    return render(request, "weight_interface/cerealcrops_post.html", context)


@login_required
@csrf_exempt
def get_update_detail_cerealcrop(request, pk):
    cerealcrop = get_object_or_404(CerealCrops, pk=pk)
    if request.method == "POST":
        form = CerealCropsForm(request.POST, instance=cerealcrop)
        if form.is_valid():
            form.save()
            return redirect("cerealcrops")
    else:
        form = CerealCropsForm(instance=cerealcrop)
    return render(request, "weight_interface/cerealcrop_detail.html", {"form": form,
                                                                       "cerealcrop": cerealcrop})


@login_required
@csrf_exempt
def delete_cerealcrop(request, pk):
    cerealcrop = get_object_or_404(CerealCrops, pk=pk)
    if request.method == "POST":
        cerealcrop.delete()
        return redirect("cerealcrops")


@login_required
@csrf_exempt
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


@login_required
@csrf_exempt
def post_logshippedproduct(request):
    datetime_now = datetime.now().strftime('%Y-%m-%d')
    error = ""
    if request.method == "POST":
        form = LogShippedProdForm(request.POST)
        if form.is_valid():
            logshippedproduct = form.save(commit=False)
            logshippedproduct.save()
            return redirect("log_shipped_products")
        else:
            error = "Form don`t valid"
    form = LogShippedProdForm()
    context = {
        "form": form,
        "error": error,
        "datetime_now": datetime_now
    }
    return render(request, "weight_interface/log_shipped_products_post.html", context)


@login_required
@csrf_exempt
def get_update_detail_logshippedproduct(request, pk):
    logshippedproduct = get_object_or_404(LogShippedProducts, pk=pk)
    if request.method == "POST":
        form = LogShippedProdForm(request.POST, instance=logshippedproduct)
        if form.is_valid():
            form.save()
            return redirect("log_shipped_products")
    else:
        form = LogShippedProdForm(instance=logshippedproduct)
    return render(request, "weight_interface/log_shipped_products_detail.html", {"form": form,
                                                                                 "logshippedproduct": logshippedproduct})


@login_required
@csrf_exempt
def delete_logshippedproduct(request, pk):
    logshippedproduct = get_object_or_404(LogShippedProducts, pk=pk)
    if request.method == "POST":
        logshippedproduct.delete()
        return redirect("log_shipped_products")


@login_required
@csrf_exempt
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


@login_required
@csrf_exempt
def post_auxiliarymaterial(request):
    datetime_now = datetime.now().strftime('%Y-%m-%d')
    error = ""
    if request.method == "POST":
        form = AuxiliaryMaterialsForm(request.POST)
        if form.is_valid():
            auxiliarymaterial = form.save(commit=False)
            auxiliarymaterial.save()
            return redirect("auxiliarymaterials")
        else:
            error = "Form don`t valid"
    form = AuxiliaryMaterialsForm()
    context = {
        "form": form,
        "error": error,
        "datetime_now": datetime_now
    }
    return render(request, "weight_interface/auxiliarymaterials_post.html", context)


@login_required
@csrf_exempt
def get_update_detail_auxiliarymaterial(request, pk):
    auxiliarymaterial = get_object_or_404(AuxiliaryMaterials, pk=pk)
    if request.method == "POST":
        form = AuxiliaryMaterialsForm(request.POST, instance=auxiliarymaterial)
        if form.is_valid():
            form.save()
            return redirect("auxiliarymaterials")
    else:
        form = AuxiliaryMaterialsForm(instance=auxiliarymaterial)
    return render(request, "weight_interface/auxiliarymaterials_detail.html", {"form": form,
                                                                               "auxiliarymaterial": auxiliarymaterial})


@login_required
@csrf_exempt
def delete_auxiliarymaterial(request, pk):
    auxiliarymaterial = get_object_or_404(AuxiliaryMaterials, pk=pk)
    if request.method == "POST":
        auxiliarymaterial.delete()
        return redirect("auxiliarymaterials")
