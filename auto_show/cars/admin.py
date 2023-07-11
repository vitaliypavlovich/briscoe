from django.contrib import admin

from cars.models import Car, Color, Wheel, Interior, Seat, CarModel
from cars.models import Purchase


class PurchaseAdminInline(admin.StackedInline):
    model = Purchase


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "image",
        "price",
        "price_usd",
        "description",
        "created_at",
    )
    fields = (
        "title",
        "category",
        "image",
        "price",
        "price_usd",
        "description",
        "created_at",
    )
    readonly_fields = ("created_at",)
    search_fields = (
        "title",
        "category",
        "price",
        "price_usd",
    )
    inlines = (PurchaseAdminInline,)

    def save_form(self, request, form, change):
        return super().save_form(request, form, change)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("car", "title", "image", "created_at")
    fields = ("car", "title", "image", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title",)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("car", "title", "image", "price_usd", "created_at")
    fields = ("car", "title", "image", "price_usd", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "price_usd",)


@admin.register(Wheel)
class WheelAdmin(admin.ModelAdmin):
    list_display = ("car", "title", "image", "price_usd", "created_at")
    fields = ("car", "title", "image", "price_usd", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "price_usd",)


@admin.register(Interior)
class InteriorAdmin(admin.ModelAdmin):
    list_display = ("car", "title", "image", "price_usd", "created_at")
    fields = ("car", "title", "image", "price_usd", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "price_usd",)


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("car", "title", "image", "price_usd", "created_at")
    fields = ("car", "title", "image", "price_usd", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "price_usd",)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "car", "color", "wheel", "interior", "seat", "price", "price_usd", "count", "created_at")
    fields = ("user", "car", "color", "wheel", "interior", "seat", "price", "price_usd", "count", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user__email", "car__title")
