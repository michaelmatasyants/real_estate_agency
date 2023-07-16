# Generated by Django 2.2.24 on 2023-07-12 11:54

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='construction_year',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Год постройки здания:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Когда создано объявление:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='description',
            field=models.TextField(blank=True, verbose_name='Текст объявления:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.CharField(help_text='Первый этаж, последний этаж, пятый этаж', max_length=3, verbose_name='Этаж:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='has_balcony',
            field=models.NullBooleanField(db_index=True, verbose_name='Наличие балкона:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='living_area',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Количество жилых кв.метров:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(null=True, verbose_name='Новостройка:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner',
            field=models.CharField(max_length=200, verbose_name='ФИО владельца:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owners_phonenumber',
            field=models.CharField(max_length=20, verbose_name='Номер владельца:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='price',
            field=models.IntegerField(db_index=True, verbose_name='Цена квартиры:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='rooms_number',
            field=models.IntegerField(db_index=True, verbose_name='Количество комнат в квартире:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='town',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Город, где находится квартира:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='town_district',
            field=models.CharField(blank=True, help_text='Чертаново Южное', max_length=50, verbose_name='Район города, где находится квартира:'),
        ),
    ]
