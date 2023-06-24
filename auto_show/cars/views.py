import logging
from django.core.cache import cache
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import AddCarForm

logger = logging.getLogger(__name__)


def index(request):
    cars = Car.objects.all()
    title = request.GET.get("title")
    if title is not None:
        cars = cars.filter(title__icontains=title)
    purchases__count = request.GET.get("purchases__count")
    if purchases__count is not None:
        cars = cars.filter(purchases__count=purchases__count)

    response = render(request, "index.html", {"cars": cars})
    cache.set(f"cars-view-{title}-{purchases__count}", response, 60 * 60)
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

