import logging
from django.core.cache import cache
from django.shortcuts import render, redirect
from cars.models import Car, CarModel
from cars.forms import AddCarForm
from django.db.models import Q

logger = logging.getLogger(__name__)


def car_models(request):
    cars_models = CarModel.objects.filter(Q(car__id=21) | Q(car__id=47) | Q(car__id=33) |
                                          Q(car__id=72) | Q(car__id=11) | Q(car__id=15))
    response = render(request, "car_models.html", {"cars_models": cars_models})
    cache.set(f"cars_models-view-{cars_models}", response, 60 * 60)
    return response


def taycan_models(request):
    cars = Car.objects.filter(title__startswith="Taycan").order_by("created_at")
    response = render(request, "taycan_models.html", {"cars": cars})
    cache.set(f"cars-view-{cars}", response, 60 * 60)
    return response


def nine_hundred_eleven_models(request):
    cars = Car.objects.filter(title__startswith="911").order_by("created_at")
    response = render(request, "911_models.html", {"cars": cars})
    cache.set(f"cars-view-{cars}", response, 60 * 60)
    return response


def seven_hundred_eighteen_models(request):
    cars = Car.objects.filter(title__startswith="718").order_by("created_at")
    response = render(request, "718_models.html", {"cars": cars})
    cache.set(f"cars-view-{cars}", response, 60 * 60)
    return response


def panamera_models(request):
    cars = Car.objects.filter(title__startswith="Panamera").order_by("created_at")
    response = render(request, "panamera_models.html", {"cars": cars})
    cache.set(f"cars-view-{cars}", response, 60 * 60)
    return response


def macan_models(request):
    cars = Car.objects.filter(title__startswith="Macan").order_by("created_at")
    response = render(request, "macan_models.html", {"cars": cars})
    cache.set(f"cars-view-{cars}", response, 60 * 60)
    return response


def cayenne_models(request):
    cars = Car.objects.filter(title__startswith="Cayenne").order_by("created_at")
    response = render(request, "cayenne_models.html", {"cars": cars})
    cache.set(f"cars-view-{cars}", response, 60 * 60)
    return response


def add_car(request):
    if request.method == "POST":
        form = AddCarForm(request.POST)
        if form.is_valid():
            Car.objects.create(
                title=form.cleaned_data["title"],
                price=form.cleaned_data["price"],
                description=form.cleaned_data["description"],
            )
            logger.info(f"Car name: {form.cleaned_data['title']}")
            logger.info(f"Car price: {form.cleaned_data['price']}")
            return redirect("/")
    else:
        form = AddCarForm()

    return render(request, "add_car.html", {"form": form})

