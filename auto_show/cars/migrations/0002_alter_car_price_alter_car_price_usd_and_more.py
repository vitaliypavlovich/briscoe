# Generated by Django 4.1.7 on 2023-06-24 22:20

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="price",
            field=models.DecimalField(
                decimal_places=4, default=Decimal("0"), max_digits=10
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="price_usd",
            field=models.DecimalField(
                decimal_places=4, default=Decimal("0"), max_digits=10
            ),
        ),
        migrations.AlterField(
            model_name="purchase",
            name="price",
            field=models.DecimalField(
                decimal_places=4, default=Decimal("0"), max_digits=10
            ),
        ),
        migrations.AlterField(
            model_name="purchase",
            name="price_usd",
            field=models.DecimalField(
                decimal_places=4, default=Decimal("0"), max_digits=10
            ),
        ),
    ]
