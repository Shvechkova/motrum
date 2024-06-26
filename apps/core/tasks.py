import datetime
from urllib.request import urlopen
import xml.etree.ElementTree as ET
from xml.etree import ElementTree, ElementInclude

from apps.core.models import Currency
from apps.product.models import CurrencyRate, Price
from apps.specification.models import Specification
from project.celery import app


@app.task(
    bind=True,
    max_retries=10,
)
def get_currency(self):
  
    try:
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
            print(value)
            v = float(value.replace(",", "."))
            vi = float(vunit_rate.replace(",", "."))

            now_rate = CurrencyRate.objects.get_or_create(
                currency=current ,
                date=date,
                defaults={"value": v, "vunit_rate": vi, "count": int(count)},
            )
            update_currency_price(current, current_world_code)
            currency_chek(current, now_rate[0])

    except Exception as exc:
        self.retry(exc=exc, countdown=5)


# удаление старых курсов
def del_currency():
    print(1231231)
    now = datetime.datetime.now()
    three_days = datetime.timedelta(3)
    in_three_days = now - three_days
    data = in_three_days.strftime("%Y-%m-%d")
    CurrencyRate.objects.filter(date__lt=data).delete()


# обновление валютных цен у всех продуктов
def update_currency_price(currency, current_world_code):
    products = Price.objects.filter(currency=currency)
    for product in products:
        p = Price.objects.get(id=product.id)
        p.save()


# проверка на увелисеие курса на 3% -если да отмерка спецификации не действительны
def currency_chek(current, now_rate):
    old_rate = CurrencyRate.objects.filter(
        currency=current,
    ).earliest("date")
    old_rate_count = old_rate.vunit_rate
    new_rate_count = now_rate.vunit_rate
    # print(new_rate_count)
    difference_count = old_rate_count - new_rate_count

    count_percent = old_rate_count / 100 * 3
    # print(difference_count)
    # print(count_percent)
    if difference_count > count_percent:
        specification = Specification.objects.filter(
            tag_stop=True, tag_currency_id=now_rate.currency.id
        ).update(tag_stop=False)
