import logging
from django.core.cache import cache
from django.shortcuts import render, redirect
from cars.models import Car, CarModel
from cars.forms import AddCarForm

logger = logging.getLogger(__name__)


def index(request):
    cars_models = CarModel.objects.all()
    title = request.GET.get("title")
    if title is not None:
        cars_models = cars_models.filter(title__icontains=title)

    response = render(request, "index.html", {"cars_models": cars_models})
    cache.set(f"cars_models-view-{title}", response, 60 * 60)
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

