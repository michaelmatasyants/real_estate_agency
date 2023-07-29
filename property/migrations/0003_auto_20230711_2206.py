# Generated by Django 2.2.24 on 2023-07-11 19:06

from django.db import migrations


def fill_field_new_building(apps, scema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.filter(new_building=None):
        if flat.construction_year >= 2015:
            flat.new_building = True
            flat.save()
            continue
        flat.new_building = False
        flat.save()

    Flat.objects.filter(new_building=None, construction_year__gte=2015).update(
         new_building=True)
    Flat.objects.filter(new_building=None, construction_year__lt=2015).update(
         new_building=False)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20230711_2131'),
    ]

    operations = [
        migrations.RunPython(fill_field_new_building)
    ]
