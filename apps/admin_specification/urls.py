from django.urls import include, path

from django.urls import re_path as url
from . import views


app_name = "admin_specification"


urlpatterns = [
    path("", views.specifications, name="specifications"),
]
