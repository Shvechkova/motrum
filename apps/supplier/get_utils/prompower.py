import datetime
import os
import traceback
import requests
import json
from simple_history.utils import update_change_reason
from apps import supplier
from project.settings import MEDIA_ROOT

from apps.core.models import Currency, Vat
from apps.core.utils import (
    create_article_motrum,
    get_category_prompower,
    get_file_path_add,
    save_file_product,
    save_update_product_attr,
)
from apps.logs.utils import error_alert
from apps.product.models import (
    Lot,
    Price,
    Product,
    ProductDocument,
    ProductImage,
    ProductProperty,
    Stock,
)
from apps.supplier.models import (
    Supplier,
    SupplierCategoryProduct,
    SupplierCategoryProductAll,
    SupplierGroupProduct,
    Vendor,
)


def prompower_api():
    prompower = Supplier.objects.get(slug="prompower")
    vendors = Vendor.objects.filter(slug="prompower")
    for vendors_item in vendors:
        if vendors_item.slug == "prompower":
            vendoris = vendors_item

    # ОБЩАЯ КАТЕГОРИЯ
    def add_category_groupe():
        url = "https://prompower.ru/api/getCategoryGroups"
        headers = {
            "Cookie": "auth.strategy=local; nuxt-session-id=s%3AVh_wHm_Gp554xfQDqHV6CDxDRMUx5ZH6.NDr1rbwGm%2Boj%2FzU5JLtPnug2OErY%2BhDm9%2FCTOi9r0bM"
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
        )
        data = response.json()

        for data_item in data:
            
            try:
                categ = SupplierCategoryProduct.objects.get(
                    supplier=prompower,
                    vendor=vendoris,
                    article_name=data_item["id"],
                )
                if categ.name != data_item["title"]:
                    categ.name = data_item["title"]
                    categ.save()
                

            except SupplierCategoryProduct.DoesNotExist:
                categ = SupplierCategoryProduct(
                    supplier=prompower,
                    vendor=vendoris,
                    article_name=data_item["id"],
                    name=data_item["title"],
                )
                categ.save()

    # получение всех категорий для каталога
    def add_category():
        url = "https://prompower.ru/api/categories"
        headers = {
            "Cookie": "nuxt-session-id=s%3ArUFByHT7pVHJLlRaku2tG74R7byS_LuK.hVBBCnWUOXqkuHRB8%2FgmCu%2BXk1ZLjQMNeYcrdoBb6O8"
        }
        response = requests.request("GET", url, headers=headers)
        data = response.json()

        # категория\группа
        for data_item in data:
            if data_item["groupId"] is not None and data_item["parentId"] is None:
                categ = SupplierCategoryProduct.objects.get(
                    supplier=prompower,
                    vendor=vendoris,
                    article_name=data_item["groupId"],
                )

                # группа
                try:
                    grope = SupplierGroupProduct.objects.get(
                        supplier=prompower,
                        vendor=vendoris,
                        article_name=data_item["id"],
                        # category_supplier=categ,
                        # name=data_item["title"],
                        # slug=data_item["slug"],
                    )
                    if grope.category_supplier != categ:
                        grope.category_supplier = categ
                    
                    if grope.slug != data_item["title"]:
                        grope.name = data_item["title"]
                        
                    if grope.name != data_item["slug"]:
                        grope.slug = data_item["slug"]    
                    
                    grope.save()

                except SupplierGroupProduct.DoesNotExist:
                    grope = SupplierGroupProduct(
                        supplier=prompower,
                        vendor=vendoris,
                        article_name=data_item["id"],
                        category_supplier=categ,
                        name=data_item["title"],
                        slug=data_item["slug"],
                    )
                    grope.save()
       # конечная группа
        for data_item_all in data:

            if data_item_all["parentId"] is not None:
                grope = SupplierGroupProduct.objects.get(
                    supplier=prompower,
                    vendor=vendoris,
                    article_name=data_item_all["parentId"],
                )

                try:
                    all_groupe = SupplierCategoryProductAll.objects.get(
                        supplier=prompower,
                        vendor=vendoris,
                        article_name=data_item_all["id"],
                        # name=data_item_all["title"],
                        # slug=data_item_all["slug"],
                    )
                    if all_groupe.name != data_item_all["title"]:
                        all_groupe.name = data_item_all["title"]
                    
                    if all_groupe.slug != data_item_all["slug"]:
                        all_groupe.slug = data_item_all["slug"]
                    
                    if all_groupe.group_supplier != data_item_all["parentId"]:
                        all_groupe.group_supplier = grope
                        all_groupe.category_supplier_id=grope.category_supplier.id
                    
                    all_groupe.save()  
                    
                        
                    

                except SupplierCategoryProductAll.DoesNotExist:
                    all_groupe = SupplierCategoryProductAll(
                        supplier=prompower,
                        vendor=vendoris,
                        name=data_item_all["title"],
                        article_name=data_item_all["id"],
                        category_supplier=grope.category_supplier,
                        group_supplier=grope,
                        slug=data_item_all["slug"],
                    )
                    all_groupe.save()

    # добавление товаров
    def add_products():
        url = "https://prompower.ru/api/prod/getProducts"
        payload = json.dumps(
            {
                "email": os.environ.get("PROMPOWER_API_EMAIL"),
                "key": os.environ.get("PROMPOWER_API_KEY"),
            }
        )
        headers = {
            "Content-type": "application/json",
            "Cookie": "nuxt-session-id=s%3Anp9ngMJIwPPIJnpKt1Xow9DA50eUD5OQ.IwH2nwSHFODHMKNUx%2FJRYeOVF9phtKXSV6dg6QQebAU",
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()

        # vendor = Vendor.objects.filter(supplier=prompower)
        vat_catalog = Vat.objects.get(name="20")
        vat_catalog_int = int(vat_catalog.name)
        currency = Currency.objects.get(words_code="RUB")
        base_adress = "https://prompower.ru"
        vendori = Vendor.objects.get(slug="prompower") 
        vendor_item = vendori
        # for vendor_item in vendor:
        #     print(1,vendor_item)
        #     if vendor_item.slug == "prompower":
        #         print(2,vendor_item)
        #         vendori = vendor_item
        #     else:
        #         vendori = Vendor.objects.filter(slug="prompower") 
          
        # print(3,vendori)
        for data_item in data:

            try:
                if data_item["article"] != None:
                    # основная инфа
                    article_suppliers = data_item["article"]
                    name = data_item["title"]
                    description = data_item["description"]

                    if "categoryId" in data_item:

                        category_all = data_item["categoryId"]
                        if category_all != 35:
                            categ = get_category_prompower(
                                prompower, vendori, category_all
                            )
                        else:
                            categ = None
                    else:
                        categ = None

                    # цены
                    price_supplier = int(data_item["price"])
                    vat_include = True
                    # остатки
                    lot = Lot.objects.get(name="штука")
                    stock_supplier = data_item["instock"]
                    lot_complect = 1

                    img_list = data_item["img"]

                    def save_image(
                        article,
                    ):

                        if len(img_list) > 0:
                            for img_item in img_list:
                                img = f"{base_adress}{img_item}"
                                image = ProductImage.objects.create(product=article)
                                update_change_reason(image, "Автоматическое")
                                image_path = get_file_path_add(image, img)
                                p = save_file_product(img, image_path)
                                image.photo = image_path
                                image.link = img
                                image.save()
                                update_change_reason(image, "Автоматическое")

                    def save_document(categ, product):
                        # документы категории
                        base_dir = "products"
                        path_name = "document_group"
                        base_dir_supplier = product.supplier.slug
                        base_dir_vendor = product.vendor.slug
                    
                        if categ[1] != None:
                            group_name = categ[1].slug
                            url = f"https://prompower.ru/api/docfiles?dir={group_name}&filenameFilter"
                            new_dir = "{0}/{1}/{2}/{3}/{4}/{5}".format(
                                MEDIA_ROOT,
                                base_dir,
                                base_dir_supplier,
                                base_dir_vendor,
                                path_name,
                                group_name,
                            )
                            if not os.path.exists(new_dir):
                                os.makedirs(new_dir)
                            dir_no_path = "{0}/{1}/{2}/{3}/{4}".format(
                                base_dir,
                                base_dir_supplier,
                                base_dir_vendor,
                                path_name,
                                group_name,
                            )
                        if categ[0] != None:
                            category_supplier = categ[0].slug
                            url = f"https://prompower.ru/api/docfiles?dir={group_name}&subdir={category_supplier}&filenameFilter"

                            new_dir = "{0}/{1}/{2}/{3}/{4}/{5}/{6}".format(
                                MEDIA_ROOT,
                                base_dir,
                                base_dir_supplier,
                                base_dir_vendor,
                                path_name,
                                group_name,
                                category_supplier,
                            )
                            dir_no_path = "{0}/{1}/{2}/{3}/{4}/{5}".format(
                                base_dir,
                                base_dir_supplier,
                                base_dir_vendor,
                                path_name,
                                group_name,
                                category_supplier,
                            )
                            if not os.path.exists(new_dir):
                                os.makedirs(new_dir)
                      
                        response = requests.request(
                            "GET",
                            url,
                        )
                        data = response.json()
                        for item_doc in data["data"]:
                            doc_item = item_doc["link"]
                            doc_link = f"{base_adress}{doc_item}"

                            doc = ProductDocument.objects.create(product=article)
                            update_change_reason(doc, "Автоматическое")
                            doc_list_name = doc_link.split("/")
                            doc_name = doc_list_name[-1]
                            images_last_list = doc_link.split(".")
                            type_file = "." + images_last_list[-1]
                            link_file = f"{new_dir}/{doc_name}"

                      

                            if os.path.isfile(link_file):
                                print("Файл существует")
                            else:
                                r = requests.get(doc_link, stream=True)
                                with open(os.path.join(link_file), "wb") as ofile:
                                    ofile.write(r.content)

                            type_doc = item_doc["type"].capitalize()
                       
                            doc.document = f"{dir_no_path}/{doc_name}"
                            doc.link = doc_link
                            doc.name = item_doc["title"]
                            doc.type_doc = item_doc["type"].capitalize()

                            doc.save()
                            update_change_reason(doc, "Автоматическое")

                        # документы индивидуальные
                        doc_list = data_item["cad"]
                        if len(doc_list) > 0:

                            for doc_item_individual in doc_list:

                                img = f"{base_adress}/catalog/CAD/{doc_item_individual["filename"]}"
                                image = ProductDocument.objects.create(product=article)
                                update_change_reason(image, "Автоматическое")
                                image_path = get_file_path_add(image, img)
                              
                                p = save_file_product(img, image_path)
                                image.photo = image_path
                                image.link = img
                                image.document = image_path
                                image.link = img
                                image.name = doc_item_individual["title"]
                                image.type_doc = "Other"
                                image.save()
                                update_change_reason(image, "Автоматическое")

                    # если товар без категории и 0 цена не сохранять
                    if price_supplier != "0" and categ != None:
                        price_supplier = price_supplier + (price_supplier / 100 * 20)
                        try:
                            # если товар есть в бд
                            article = Product.objects.get(
                                supplier=prompower,
                                vendor=vendori,
                                article_supplier=article_suppliers,
                            )

                            # если у товара не было совсем дококв из пропсов
                            props = ProductProperty.objects.filter(
                                product=article
                            ).exists()
                            if props == False:
                                for prop in data_item["props"]:
                                    property_product = ProductProperty(
                                        product=article,
                                        name=prop["name"],
                                        value=prop["value"],
                                    )
                                    property_product.save()
                                    update_change_reason(
                                        property_product, "Автоматическое"
                                    )

                            image = ProductImage.objects.filter(
                                product=article
                            ).exists()
                            if image == False:
                                save_image(article)

                            doc = ProductDocument.objects.filter(
                                product=article
                            ).exists()
                            if doc == False:
                                save_document(categ, article)

                            save_update_product_attr(
                                article,
                                supplier,
                                vendori,
                                None,
                                categ[0],
                                categ[1],
                                categ[2],
                                description,
                                name,
                            )

                        except Product.DoesNotExist:
                            # если товара нет в бд
                            new_article = create_article_motrum(prompower.id)
                            article = Product(
                                article=new_article,
                                supplier=prompower,
                                vendor=vendor_item,
                                article_supplier=article_suppliers,
                                name=name,
                                description=description,
                                category_supplier_all=categ[0],
                                group_supplier=categ[1],
                                category_supplier=categ[2],
                            )
                            article.save()
                            update_change_reason(article, "Автоматическое")
                            save_image(article)
                            save_document(categ, article)

                            for prop in data_item["props"]:
                                property_product = ProductProperty(
                                    product=article,
                                    name=prop["name"],
                                    value=prop["value"],
                                )
                                property_product.save()
                                update_change_reason(property_product, "Автоматическое")

                        # цены товара
                        try:
                            price_product = Price.objects.get(prod=article)

                        except Price.DoesNotExist:
                            price_product = Price(prod=article)

                        finally:
                            price_product.currency = currency

                            price_product.extra_price = False
                            price_product.price_supplier = price_supplier
                            price_product.vat = vat_catalog
                            price_product.vat_include = vat_include
                            price_product._change_reason = "Автоматическое"
                            price_product.save()
                            # update_change_reason(price_product, "Автоматическое")

                        # остатки
                        try:
                            stock_prod = Stock.objects.get(prod=article)
                        except Stock.DoesNotExist:
                            stock_prod = Stock(
                                prod=article,
                                lot=lot,
                            )
                        finally:
                            stock_prod.stock_supplier = stock_supplier
                            stock_prod.stock_supplier_unit = stock_supplier
                            stock_prod.data_update = datetime.datetime.now()
                            stock_prod._change_reason = "Автоматическое"
                            stock_prod.save()
                            # update_change_reason(stock_prod, "Автоматическое")

            except Exception as e:
                print(e)
                tr = traceback.format_exc()
                error = "file_api_error"
                location = "Загрузка фаилов Prompower"
                info = f"ошибка при чтении товара артикул: {data_item["article"]}. Тип ошибки:{e}{tr}"
                e = error_alert(error, location, info)
            finally:
                continue

    add_category_groupe()
    add_category()
    add_products()
    
