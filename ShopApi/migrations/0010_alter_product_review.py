<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-05-25 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApi', '0009_color_manufacturer_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ShopApi.review'),
        ),
    ]
=======
# Generated by Django 5.0.6 on 2024-05-25 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApi', '0009_color_manufacturer_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ShopApi.review'),
        ),
    ]
>>>>>>> 7bb3b2e6bebba61021555f09a5c46875067a0008
