# Generated by Django 2.2.24 on 2023-07-13 18:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20230713_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='RU', verbose_name='Номер владельца')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='RU', verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
