import datetime
from locale import LC_ALL, setlocale
import threading
from django.shortcuts import render
from apps.client.models import Order
from apps.logs.utils import error_alert
from dal import autocomplete
from django.db.models import Q

from apps.core.models import CalendarHoliday, Currency
from apps.core.tasks import currency_chek, del_currency, update_currency_price
from apps.core.utils import create_time_stop_specification
from apps.product.models import CurrencyRate, GroupProduct, Product
from apps.specification.models import Specification
from apps.supplier.get_utils.iek import get_iek_stock, iek_api
from apps.supplier.get_utils.motrum_storage import get_motrum_storage
from apps.supplier.get_utils.prompower import prompower_api
from apps.supplier.get_utils.one_c import one_c_price
from apps.supplier.get_utils.veda import veda_api
from apps.supplier.models import SupplierCategoryProductAll, Vendor
from apps.supplier.get_utils.emas import add_group_emas, add_props_emas_product
from apps.supplier.models import SupplierCategoryProduct, SupplierGroupProduct
from apps.supplier.tasks import add_veda
from apps.user.utils import upgrade_permission
from urllib.request import urlopen
import xml.etree.ElementTree as ET
from xml.etree import ElementTree, ElementInclude
from pytils import translit
from django.utils.text import slugify
from simple_history.utils import update_change_reason


# тестовая страница скриптов
def add_iek(request):

    title = "Услуги"
    iek_api()
    
    responsets = ["233", "2131"]
    # responsets = 0
    context = {
        "title": title,
        "responsets": responsets,
    }
    return render(request, "supplier/supplier.html", context)


# тестовая страница скриптов
def test(request):
    def background_task():
        # Долгосрочная фоновая задача
        iek_api()

    daemon_thread = threading.Thread(target=background_task)
    daemon_thread.setDaemon(True)
    daemon_thread.start()

    title = "Услуги"

    responsets = ["233", "2131"]

    context = {
        "title": title,
        "responsets": responsets,
    }
    return render(request, "supplier/supplier.html", context)


def add_one_c(request):
    one_c_price()
    title = "Услуги"
   

    responsets = ["233", "2131"]

    context = {
        "title": title,
        "responsets": responsets,
    }
    return render(request, "supplier/supplier.html", context)


# сохранение емас данных первичное из копии сайта фаилы должны лежать на сервере
def save_emas_props(request):

    def background_task():
        # Долгосрочная фоновая задача
        # add_group_emas()
        add_props_emas_product()

    daemon_thread = threading.Thread(target=background_task)
    daemon_thread.setDaemon(True)
    daemon_thread.start()

    responsets = ["233", "2131"]

    context = {
        "responsets": responsets,
    }
    return render(request, "supplier/supplier.html", context)


# добавление разрешений админам
def add_permission(request):
    upgrade_permission()
    context = {}
    return render(request, "supplier/supplier.html", context)


# добавление праздников вручную
def add_holidays(request):
    import json
    import requests

    year_date = datetime.datetime.now().year
    year = str(year_date)
    url = (
        "https://raw.githubusercontent.com/d10xa/holidays-calendar/master/json/consultant"
        + year
        + ".json"
    )
    r = requests.get(url)
    holidays_dict = r.json()

    try:
        data_bd = CalendarHoliday.objects.get(year=year)
        data_bd.json_date = holidays_dict
        data_bd.save()

    except CalendarHoliday.DoesNotExist:

        data_bd = CalendarHoliday(year=year, json_date=holidays_dict)
        data_bd.save()

    context = {}
    return render(request, "supplier/supplier.html", context)


# получение валют вручную
def get_currency(request):
    del_currency()
    currency_list = Currency.objects.exclude(words_code="RUB")
    resp = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = urlopen(resp)
    item = ET.parse(response)
    root = item.getroot()
    ElementInclude.include(root)
    date = datetime.datetime.now()
    for current in currency_list:
        current_world_code = current.words_code
        value = item.findtext(f".//Valute[CharCode='{current_world_code}']/Value")
        vunit_rate = item.findtext(
            f".//Valute[CharCode='{current_world_code}']/VunitRate"
        )
        count = item.findtext(f".//Valute[CharCode='{current_world_code}']/Nominal")

        v = float(value.replace(",", "."))
        vi = float(vunit_rate.replace(",", "."))

        now_rate = CurrencyRate.objects.get_or_create(
            currency=current,
            date=date,
            defaults={"value": v, "vunit_rate": vi, "count": int(count)},
        )
        update_currency_price(current, current_world_code)
        currency_chek(current, now_rate[0])
    context = {}
    return render(request, "supplier/supplier.html", context)


class VendorAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Vendor.objects.all()

        supplier = self.forwarded.get("supplier", None)
        if supplier:
            qs = qs.filter(supplier=supplier)

        vendor = self.forwarded.get("vendor", None)
        if vendor:
            qs = qs.filter(vendor=vendor)

        return qs


class SupplierCategoryAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = SupplierCategoryProduct.objects.all()

        supplier = self.forwarded.get("supplier", None)
        if supplier:
            qs = qs.filter(supplier=supplier)

        vendor = self.forwarded.get("vendor", None)
        if vendor:
            qs = qs.filter(vendor=vendor)

        return qs


class SupplierGroupAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = SupplierGroupProduct.objects.all()
        supplier = self.forwarded.get("supplier", None)

        if supplier:
            qs = qs.filter(supplier=supplier)

        vendor = self.forwarded.get("vendor", None)
        if vendor:
            qs = qs.filter(vendor=vendor)

        category_supplier = self.forwarded.get("category_supplier", None)
        if category_supplier:
            qs = qs.filter(category_supplier=category_supplier)

        if self.q:
            qs = qs.filter(
                Q(name__icontains=self.q) | Q(article_name__icontains=self.q)
            )
        return qs


# class SupplierGroupСategoryAutocomplete(autocomplete.Select2QuerySetView):

#     def get_queryset(self):
#         qs = SupplierGroupProduct.objects.all()
#         supplier = self.forwarded.get("supplier", None)

#         if supplier:
#             qs = qs.filter(supplier=supplier)

#         vendor = self.forwarded.get("vendor", None)
#         if vendor:
#             qs = qs.filter(vendor=vendor)

#         category_supplier = self.forwarded.get("category_supplier", None)
#         if category_supplier:
#             qs = qs.filter(category_supplier=category_supplier)

#         if self.q:
#             qs = qs.filter(
#                 Q(name__icontains=self.q)
#                 | Q(article_name__icontains=self.q)
#             )
#         return qs


class SupplierCategoryProductAllAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = SupplierCategoryProductAll.objects.all()
        supplier = self.forwarded.get("supplier", None)
        if supplier:
            qs = qs.filter(supplier=supplier)

        vendor = self.forwarded.get("vendor", None)
        if vendor:
            qs = qs.filter(vendor=vendor)

        category_supplier = self.forwarded.get("category_supplier", None)
        if category_supplier:
            qs = qs.filter(category_supplier=category_supplier)

        group_supplier = self.forwarded.get("group_supplier", None)
        if category_supplier:
            qs = qs.filter(group_supplier=group_supplier)

        if self.q:
            qs = qs.filter(
                Q(name__icontains=self.q) | Q(article_name__icontains=self.q)
            )

        return qs


class GroupProductAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = GroupProduct.objects.all()
        category_catalog = self.forwarded.get("category_catalog", None)
        if category_catalog:
            qs = qs.filter(category=category_catalog)

        if self.q:
            qs = qs.filter(
                Q(name__icontains=self.q) | Q(article_name__icontains=self.q)
            )
        return qs
