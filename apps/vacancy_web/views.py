from django.shortcuts import render

from apps.vacancy_web.models import Vacancy


# Create your views here.
def vacancy(request):
    title = "Вакансии"
    vacancy = Vacancy.objects.filter(is_actual=True)
 
    context = {"title": title, "vacancy": vacancy}
    return render(request, "vacancy_web/vacancy_all.html", context)


def vacancy_item(request, slug):
    title = "Вакансия"
    vacancy = Vacancy.objects.get(slug=slug)
    context = {
        "title": title,
        "vacancy": vacancy,
    }

    return render(request, "vacancy_web/vacancy_one.html", context)
