# Generated by Django 2.2.14 on 2022-01-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_products_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='disc_price',
            field=models.IntegerField(null=True),
        ),
    ]
