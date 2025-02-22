from django.urls import include, path

from apps import product
from . import views
from django.views.generic.base import TemplateView

# from .api import view_sets
from rest_framework import routers
from django.urls import re_path as url

app_name = "core"

router = routers.DefaultRouter()


urlpatterns = [
    path("", views.index, name="index"),  # главная
    path(
        "okt/",
        TemplateView.as_view(template_name="core/okt.html"),
        name="okt",
    ),  # окт
    path("company/", views.company, name="about"),  # компания общая
    path("company/about/", views.company_about, name="about_company"),  # компания
    path("company/vacancy/", include("apps.vacancy_web.urls", namespace="vacancy")),
    # остальное по вакансии  в app vacancy_web
    path("solutions/", views.solutions_all, name="solutions"),
    path("cobots/", views.cobots_all, name="cobots"),
    path("cobots-palett/", views.solutions_one, name="cobots-palett"),
    path("cobots-box/", views.solutions_one, name="cobots-box"),
    path("cobots-packing/", views.solutions_one, name="cobots-packing"),
    path("marking/", views.solutions_one, name="marking"),
    path("shkaf-upravleniya/", views.solutions_one, name="shkaf-upravleniya"),
    path(
        "contact/",
        TemplateView.as_view(template_name="core/contact.html"),
        name="contact",
    ),  # контакты
    path("cart/", views.cart, name="cart"),  # корзина
    path(
        "privacy-policy/", views.privacy_policy, name="privacy-policy"
    ),  # политика конфиденциальности
    path("brand/", product.views.brand_all, name="brand"),
    path("brand/<slug:vendor>/", product.views.brand_one, name="brand_one"),
    path("add_admin_okt/", views.add_admin_okt, name="add_admin_okt"),
    # path("cart", views.cart,name="cart"),
    # path("/cart", include("apps.client.urls", namespace="cart")),
    # проекты в app project_web namespace="project"
    # каталог и товар  в app product
    # личный кабинет   в  app client  namespace="lk"
    # EMAILS
    # EMAILS
    # path("send_email_callback", views.email_callback, name="send_email_callback"),
    # path("send_email_manager", views.email_manager, name="send_email_manager"),
]
