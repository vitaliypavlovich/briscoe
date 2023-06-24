# Generated by Django 4.1.7 on 2023-06-24 21:38

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "external_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("title", models.CharField(max_length=255)),
                ("image", models.ImageField(blank=True, null=True, upload_to="cars/")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=5, default=Decimal("0"), max_digits=10
                    ),
                ),
                (
                    "price_usd",
                    models.DecimalField(
                        decimal_places=5, default=Decimal("0"), max_digits=10
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[("NEW", "New"), ("WITH_MILEAGE", "With_mileage")],
                        default="NEW",
                        max_length=32,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name="Wheel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("image", models.ImageField(blank=True, null=True, upload_to="cars/")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wheels",
                        to="cars.car",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Seat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("image", models.ImageField(blank=True, null=True, upload_to="cars/")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seats",
                        to="cars.car",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Purchase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=5, default=Decimal("0"), max_digits=10
                    ),
                ),
                (
                    "price_usd",
                    models.DecimalField(
                        decimal_places=5, default=Decimal("0"), max_digits=10
                    ),
                ),
                ("count", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchases",
                        to="cars.car",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchases",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Interior",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("image", models.ImageField(blank=True, null=True, upload_to="cars/")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interiors",
                        to="cars.car",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("image", models.ImageField(blank=True, null=True, upload_to="cars/")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="colors",
                        to="cars.car",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("image", models.ImageField(blank=True, null=True, upload_to="cars/")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="models",
                        to="cars.car",
                    ),
                ),
            ],
        ),
    ]
