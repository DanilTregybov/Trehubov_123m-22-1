# Generated by Django 4.2.5 on 2023-11-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxiliarymaterials',
            name='Time_1st_weighing',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='auxiliarymaterials',
            name='Time_2nd_weighing',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='cerealcrops',
            name='Check_in_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='cerealcrops',
            name='Departure_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='logshippedproducts',
            name='Departure_time',
            field=models.TimeField(),
        ),
    ]