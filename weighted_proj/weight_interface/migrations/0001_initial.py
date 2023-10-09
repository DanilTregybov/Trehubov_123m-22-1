# Generated by Django 4.2.5 on 2023-10-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuxiliaryMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Product_name', models.CharField(max_length=150)),
                ('Supplier', models.CharField(max_length=150)),
                ('Car_license_plate', models.CharField(max_length=15)),
                ('Trailer_license_plate', models.CharField(max_length=15)),
                ('Time_1st_weighing', models.TimeField()),
                ('Gross_weight_kilos', models.FloatField()),
                ('Time_2nd_weighing', models.TimeField()),
                ('Tare_weight_kilos', models.FloatField()),
                ('Net_weight_kilos', models.FloatField()),
                ('Weight_on_invoice_kilos', models.FloatField()),
                ('Surplus', models.FloatField()),
                ('Lack_of', models.FloatField()),
                ('Driver', models.CharField(max_length=80)),
                ('Weightman', models.CharField(max_length=80)),
                ('Number_of_CN', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CerealCrops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Supplier', models.CharField(max_length=150)),
                ('Place_of_download', models.CharField(max_length=350)),
                ('Recipient', models.CharField(max_length=150)),
                ('Delivery_condition', models.CharField(max_length=10)),
                ('Analysis_number', models.IntegerField()),
                ('Number_of_CN', models.IntegerField()),
                ('Car_license_plate', models.CharField(max_length=15)),
                ('Trailer_license_plate', models.CharField(max_length=15)),
                ('Gross_weight_kilos', models.FloatField()),
                ('Tare_weight_kilos', models.FloatField()),
                ('Weight_on_invoice_kilos', models.FloatField()),
                ('Actual_weight', models.FloatField()),
                ('Lack_of', models.FloatField()),
                ('Driver', models.CharField(max_length=80)),
                ('Driver_phone', models.CharField(max_length=40)),
                ('Carrier', models.CharField(max_length=150)),
                ('Check_in_time', models.TimeField()),
                ('Departure_time', models.TimeField()),
                ('Weightman', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='LogShippedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.BooleanField(default=False)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Customer', models.CharField(max_length=150)),
                ('Product', models.CharField(max_length=150)),
                ('Current_container', models.CharField(max_length=150)),
                ('Tare_weight_kilos', models.FloatField()),
                ('Net_weight_kilos', models.FloatField()),
                ('Price', models.IntegerField()),
                ('Driver', models.CharField(max_length=80)),
                ('Driver_phone', models.CharField(max_length=40)),
                ('Unloading_point', models.CharField(max_length=350)),
                ('Car_license_plate', models.CharField(max_length=15)),
                ('Trailer_license_plate', models.CharField(max_length=15)),
                ('Departure_time', models.TimeField()),
                ('Weightman', models.CharField(max_length=80)),
            ],
        ),
    ]
