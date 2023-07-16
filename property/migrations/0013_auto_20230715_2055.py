# Generated by Django 2.2.24 on 2023-07-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_connect_owner_and_flat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_deprecated',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='owner',
            name='owned_flats',
            field=models.ManyToManyField(db_index=True, related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
