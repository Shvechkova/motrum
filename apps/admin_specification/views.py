from django.shortcuts import render
from apps.product.models import Product
from django.core.paginator import Paginator

# Create your views here.


def specifications(request):
    product_list = Product.objects.select_related(
        "supplier",
        "vendor",
        "category_supplier_all",
        "group_supplier",
        "category_supplier",
        "category",
        "group",
        "price",
        "historic_stock",
    ).all()

    title = "Услуги"

    pagintation_list = []
    for produt_item in product_list:
        pagintation_list.append(produt_item)
    paginator = Paginator(pagintation_list, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    num_of_pages = paginator.num_pages
    context = {
        "title": title,
        "products": page_obj,
        "num_of_pages": num_of_pages,
    }
    return render(request, "admin_specification/specification_page.html", context)
