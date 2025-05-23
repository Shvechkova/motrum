from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.urls import reverse
from apps.user.forms import LoginAdminForm
from apps.user.models import AdminUser
from django.views.decorators.csrf import csrf_exempt


# логин админа
@csrf_exempt
def login_admin(request):
    form = LoginAdminForm()
    next_url = request.POST.get("next")
    id_bitrix = request.GET.get("id_bitrix")

    # если логин через битрикс
    if id_bitrix:
        redirects = login_bitrix(request, next_url, id_bitrix)
        return redirects

    # если вход не через битрикс
    else:
        if request.method == "POST":
            # после войти в форме входа
            redirects = login_clear(request, next_url, form)
            return redirects
        # форма входа
        else:
            context = {
                "error": "",
            }
            return form_login(request, context, form)


# разлогин админа
@csrf_exempt
def logout_admin(request):
    logout(request)

    response = redirect(reverse("user:login_admin") + "?next=/admin_specification/")
    response.set_cookie("client_id", max_age=-1)
    response.set_cookie("cart", max_age=-1)
    response.set_cookie("specificationId", max_age=-1)
    response.set_cookie("order", max_age=-1)
    response.set_cookie("type_save", max_age=-1)
    response.set_cookie(
        "next_url",
        max_age=-1,
        samesite="None",
        secure=True,
    )

    response.set_cookie(
        "bitrix_id_order",
        max_age=-1,
        samesite="None",
        secure=True,
    )
    response.set_cookie(
        "order",
        max_age=-1,
        samesite="None",
        secure=True,
    )
    response.set_cookie(
        "type_save",
        max_age=-1,
        samesite="None",
        secure=True,
    )
    return response
    # return redirect(reverse("user:login_admin") + "?next=/admin_specification/")


# форма для логина
@csrf_exempt
def form_login(request, context, form):
    return render(request, "user/login_admin.html", {"form": form, "context": context})


@csrf_exempt
def login_clear(request, next_url, form):

    form = LoginAdminForm(request.POST)
    if next_url == None:
        next_url = "/admin_specification/"
    print(next_url)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(username=cd["username"], password=cd["password"])
        print(user)
        # если прошел аутентификация
        if user is not None:
            # если не заблокирова
            if user.is_active:
                login(request, user)
                is_groups_user = user.groups.filter(
                    name__in=["Полный доступ", "Базовый доступ"]
                ).exists()

                # если есть право на просмотр спецификаций
                if is_groups_user == True:
                    cookie = request.COOKIES.get("client_id")
                    cookie_next = request.COOKIES.get("next_url")
                    if cookie_next:
                        next_url = cookie_next

                    response = redirect(next_url)
                    # response.set_cookie('client_id', max_age=-1)
                    # response.set_cookie('cart', max_age=-1)
                    # response.set_cookie('specificationId', max_age=-1)
                    # response.set_cookie('order', max_age=-1)
                    # response.set_cookie('type_save', max_age=-1)
                    # response.set_cookie(
                    #         "next_url",
                    #         max_age=-1,
                    #         samesite="None",
                    #         secure=True,
                    #     )

                    # response.set_cookie(
                    #         "bitrix_id_order",
                    #         max_age=-1,
                    #         samesite="None",
                    #         secure=True,
                    #     )
                    # response.set_cookie(
                    #         "order",
                    #         max_age=-1,
                    #         samesite="None",
                    #         secure=True,
                    #     )
                    # response.set_cookie(
                    #         "type_save",
                    #         max_age=-1,
                    #         samesite="None",
                    #         secure=True,
                    #     )

                    return response
                    # if cookie:
                    #     response = redirect(next_url) # replace redirect with HttpResponse or render
                    #     response.set_cookie('client_id', cookie, max_age=-1)

                    #     return response
                    # else:
                    #     return response
                    # return HttpResponseRedirect(next_url)

                # нет права на спецификации
                else:
                    request.GET._mutable = True
                    request.GET["next"] = next_url
                    context = {
                        "error": "У вас нет прав доступа ",
                    }
                    return render(
                        request,
                        "user/login_admin.html",
                        {"form": form, "context": context},
                    )

            # заблокирован пользователь
            else:
                request.GET._mutable = True
                request.GET["next"] = next_url
                context = {
                    "error": "Аккаунт заблокирован",
                }
                return render(
                    request,
                    "user/login_admin.html",
                    {"form": form, "context": context},
                )
        # если отказ в аутентификации
        else:
            request.GET._mutable = True
            request.GET["next"] = next_url
            context = {
                "error": " Неверные пароль или логин",
            }
            return render(
                request, "user/login_admin.html", {"form": form, "context": context}
            )


@csrf_exempt
def login_bitrix(request, next_url, id_bitrix):

    next_url = request.GET.get("next")

    if id_bitrix == "2":
        user = AdminUser.objects.get(username="admin")
        login(request, user)
        return HttpResponseRedirect(next_url)
    else:
        form = LoginAdminForm()
        context = {
            "error": "Ошибка доступа из Битрикс. Пожалуйста авторизуйтесь заново",
        }
        return form_login(request, context, form)


@csrf_exempt
def logout_clear_info(request):
    logout(request)
    response = render(
        request,
        "user/user_clear.html",
    )
    response.set_cookie("client_id", max_age=-1)
    response.set_cookie("cart", max_age=-1)
    response.set_cookie("specificationId", max_age=-1)
    response.set_cookie("order", max_age=-1)
    response.set_cookie("type_save", max_age=-1)
    response.set_cookie(
        "next_url",
        max_age=-1,
        samesite="None",
        secure=True,
    )

    response.set_cookie(
        "bitrix_id_order",
        max_age=-1,
        samesite="None",
        secure=True,
    )
    response.set_cookie(
        "order",
        max_age=-1,
        samesite="None",
        secure=True,
    )
    response.set_cookie(
        "type_save",
        max_age=-1,
        samesite="None",
        secure=True,
    )
    response.set_cookie(
        "specificationId",
        max_age=-1,
        samesite="None",
        secure=True,
    )
    response.set_cookie(
        "cart",
        max_age=-1,
        samesite="None",
        secure=True,
    )
    return response
