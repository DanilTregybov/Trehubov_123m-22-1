from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import CerealCropsForm
from .models import CerealCrops, LogShippedProducts, AuxiliaryMaterials

from datetime import datetime


# def current_datetime(request):
#     current_datetime = datetime.now()
#     return render(request, 'current_datetime.html', {'datetime': current_datetime})
# Create your views here.
@login_required
def home(request):
    return render(request, "weight_interface/base.html")


@login_required
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
def get_update_detail_cerealcrop(request, pk):
    user = request.user
    if user.is_admin:
        cerealcrop = get_object_or_404(CerealCrops, pk=pk)
        if request.method == "POST":
            form = CerealCropsForm(request.POST, instance=cerealcrop)
            if form.is_valid():
                form.save()
                return redirect("cerealcrops")
        else:
            form = CerealCropsForm(instance=cerealcrop)
        return render(request, "weight_interface/cerealcrop_detail.html", {"form": form, "cerealcrop": cerealcrop})
    else:
        return redirect("cerealcrops_list")

@login_required
def delete_cerealcrop(request, pk):
    user = request.user
    cerealcrop = get_object_or_404(CerealCrops, pk=pk)
    if user.is_admin:
        if request.method == "POST":
            cerealcrop.delete()
            return redirect("cerealcrops_list")
    else:
        return redirect("cerealcrops_list")

@login_required
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
def get_update_detail_logshippedproducts(request, pk):
    log_shipped_product = get_object_or_404(LogShippedProducts, pk=pk)  # нет темплейта
    return render(request, "weight_interface/log_shipped_product_detail.html",
                  {"log_shipped_product": log_shipped_product})

@login_required
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



