# Generated by Django 4.2.5 on 2023-11-24 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_interface', '0003_remove_auxiliarymaterials_surplus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxiliarymaterials',
            name='Lack_of',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auxiliarymaterials',
            name='Net_weight_kilos',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auxiliarymaterials',
            name='Tare_weight_kilos',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auxiliarymaterials',
            name='Time_2nd_weighing',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auxiliarymaterials',
            name='Weight_on_invoice_kilos',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cerealcrops',
            name='Actual_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cerealcrops',
            name='Departure_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cerealcrops',
            name='Lack_of',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cerealcrops',
            name='Tare_weight_kilos',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cerealcrops',
            name='Weight_net_kilos',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logshippedproducts',
            name='Departure_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logshippedproducts',
            name='Net_weight_kilos',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logshippedproducts',
            name='Tare_weight_kilos',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
