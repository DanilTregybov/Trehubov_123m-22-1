from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CerealCrops
from django.forms import ModelForm, TextInput, Textarea, DateInput, NumberInput, TimeInput
from django.contrib.auth.models import User


class CerealCropsForm(ModelForm):
    class Meta:
        model = CerealCrops
        fields = ["Supplier", "Place_of_download", "Recipient", "Delivery_condition",
                  "Analysis_number", "Number_of_CN", "Car_license_plate", "Trailer_license_plate", "Gross_weight_kilos",
                  "Tare_weight_kilos", "Weight_on_invoice_kilos", "Weight_net_kilos", "Actual_weight", "Lack_of",
                  "Driver", "Driver_phone",
                  "Carrier", "Check_in_time", "Departure_time", "Weightman"]
        widgets = {
            "Supplier": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Place_of_download": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Recipient": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Delivery_condition": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Analysis_number": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Number_of_CN": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Car_license_plate": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Trailer_license_plate": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Gross_weight_kilos": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Tare_weight_kilos": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Weight_on_invoice_kilos": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Weight_net_kilos": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Actual_weight": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Lack_of": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Driver": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Driver_phone": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Carrier": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),
            "Check_in_time": TimeInput( attrs={
                "class": "form-control",
            }),
            "Departure_time": TimeInput( attrs={
                "class": "form-control",
            }),
            "Weightman": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter note text"
            }),

        }

