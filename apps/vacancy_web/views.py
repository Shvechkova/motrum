from django.shortcuts import render

from apps.core.models import PhotoEmoloeeInfoWeb
from apps.vacancy_web.models import (
    PhotoEducationInfoWeb,
    PhotoSportsRecreationInfoWeb,
    Vacancy,
    VacancyCategory,
)


# Create your views here.
def vacancy(request):
    title = "Карьера"
    vacancy = Vacancy.objects.filter(is_actual=True)

    category_vacancy = VacancyCategory.objects.filter(is_view=True).order_by("article")
    category_vacancy = (
        vacancy.filter()
        .order_by("vacancy_category__name")
        .distinct("vacancy_category__name")
        .values("vacancy_category__name", "vacancy_category__slug", "vacancy_category__is_view", "vacancy_category__article")
    )
    photo_motrum = PhotoEmoloeeInfoWeb.objects.all().order_by("article")
    photo_education = PhotoEducationInfoWeb.objects.all().order_by("article")
    photo_recreation = PhotoSportsRecreationInfoWeb.objects.all().order_by("article")

    context = {
        "title": title,
        "vacancy": vacancy,
        "category_vacancy": category_vacancy,
        "photo_motrum": photo_motrum,
        "photo_education": photo_education,
        "photo_recreation": photo_recreation,
        "meta_title": f"{title} | Мотрум - автоматизация производства",
    }
    print(context)
    return render(request, "vacancy_web/vacancy_all.html", context)


def vacancy_item(request, slug):
    title = "Вакансия"
    vacancy = Vacancy.objects.get(slug=slug)
    context = {
        "title": title,
        "vacancy": vacancy,
    }

    return render(request, "vacancy_web/vacancy_one.html", context)
