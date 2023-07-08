import logging
from decimal import Decimal

import requests

from django.core.management.base import BaseCommand
from django_rq import job
from django.db.models import F
from cars.models import Car

logger = logging.getLogger(__name__)


@job
def update_cars():
    response = requests.get("https://www.nbrb.by/api/exrates/rates?periodicity=0")
    result = response.json()
    item = None
    for item in result:
        if item["Cur_Abbreviation"] == "USD":
            break

    if item is not None:
        for car in Car.objects.all():
            car.price = car.price_usd * Decimal(item["Cur_OfficialRate"])
            car.save()

        Car.objects.update(price=F("price_usd") * Decimal(item["Cur_OfficialRate"]))


class Command(BaseCommand):
    help = "Update cars"

    def handle(self, *args, **options):
        update_cars()
