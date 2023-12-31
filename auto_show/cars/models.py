from django.conf import settings
from django.db import models

from decimal import Decimal



CATEGORY_CHOICES = (
    ("NEW", "New"),
    ("WITH_MILEAGE", "With_mileage"),
)


class Car(models.Model):
    external_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="cars/", blank=True, null=True)
    price = models.DecimalField(default=Decimal("0"), decimal_places=2, max_digits=10)
    price_usd = models.DecimalField(
        default=Decimal("0"), decimal_places=2, max_digits=10
    )
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default="NEW")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Car: {self.title} - {self.price_usd}"


class CarModel(models.Model):
    car = models.ForeignKey(
        "cars.Car", on_delete=models.CASCADE, related_name="models"
    )
    title = models.CharField(max_length=255)
    price_usd = models.DecimalField(default=Decimal("0"), decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="cars_models/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Car model: {self.title}"


class Color(models.Model):
    car = models.ForeignKey(
        "cars.Car", on_delete=models.CASCADE, related_name="colors"
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="colors/", blank=True, null=True)
    price_usd = models.DecimalField(
        default=Decimal("0"), decimal_places=2, max_digits=10
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Color: {self.title} - {self.price_usd}"


class Wheel(models.Model):
    car = models.ForeignKey(
        "cars.Car", on_delete=models.CASCADE, related_name="wheels"
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="wheels/", blank=True, null=True)
    price_usd = models.DecimalField(
        default=Decimal("0"), decimal_places=2, max_digits=10
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Wheels: {self.title} - {self.price_usd}"


class Interior(models.Model):
    car = models.ForeignKey(
        "cars.Car", on_delete=models.CASCADE, related_name="interiors"
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="interiors/", blank=True, null=True)
    price_usd = models.DecimalField(
        default=Decimal("0"), decimal_places=2, max_digits=10
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Interior: {self.title} - {self.price_usd}"


class Seat(models.Model):
    car = models.ForeignKey(
        "cars.Car", on_delete=models.CASCADE, related_name="seats"
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="seats/", blank=True, null=True)
    price_usd = models.DecimalField(
        default=Decimal("0"), decimal_places=2, max_digits=10
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Seats: {self.title} - {self.price_usd}"


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchases"
    )
    car = models.ForeignKey(
        "cars.Car", on_delete=models.CASCADE, related_name="purchases"
    )
    color = models.ForeignKey(
        "cars.Color", on_delete=models.CASCADE, related_name="purchases", blank=True, null=True
    )
    wheel = models.ForeignKey(
        "cars.Wheel", on_delete=models.CASCADE, related_name="purchases", blank=True, null=True
    )
    interior = models.ForeignKey(
        "cars.Interior", on_delete=models.CASCADE, related_name="purchases", blank=True, null=True
    )
    seat = models.ForeignKey(
        "cars.Seat", on_delete=models.CASCADE, related_name="purchases", blank=True, null=True
    )
    price = models.DecimalField(default=Decimal("0"), decimal_places=2, max_digits=10)
    price_usd = models.DecimalField(
        default=Decimal("0"), decimal_places=2, max_digits=10
    )
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Purchase: {self.user} - {self.car} - {self.price_usd} - {self.count}"

