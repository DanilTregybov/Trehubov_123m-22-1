from django.shortcuts import render, redirect, get_object_or_404

from .models import CerealCrops


# Create your views here.
def home(request):
    return render(request, "weight_interface/base.html")
def get_cerealcrops(request):
    cerealcrops = CerealCrops.objects.all()
    return render(request, "weight_interface/cerealcrops_list.html", {"cerealcrops": cerealcrops})

def get_update_detail_cerealcrop(request, pk):
    cerealcrop = get_object_or_404(CerealCrops, pk=pk)
    return render(request, "weight_interface/cerealcrop_detail.html", {"cerealcrop": cerealcrop})
