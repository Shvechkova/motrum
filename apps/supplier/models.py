from math import prod
import os
from django.db import models
import requests
import json
from django.utils.text import slugify
from pytils import translit


from apps.core.models import Currency, Vat
# from apps.core.utils import get_file_path_add


# from apps.product.models import CategoryProduct, Product


# Create your models here.


class Supplier(models.Model):
    name = models.CharField("Название поставщика", max_length=40)
    # integration_type (тип интеграции)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"



    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug_text = self.name
        slugish = translit.translify(slug_text)
        self.slug = slugify(slugish)

        super().save(*args, **kwargs)



class Vendor(models.Model):
    
    name = models.CharField("Название производителя", max_length=40)
    slug = models.SlugField(null=True)
    supplier = models.ForeignKey(
        Supplier,
        verbose_name="Поставщик",
        on_delete=models.PROTECT,
    )
    
    currency_catalog = models.ForeignKey(
        Currency,
        verbose_name="Валюта каталога",
        on_delete=models.PROTECT,
    )
    vat_catalog = models.ForeignKey(
        Vat,
        verbose_name="Ндс в каталоге",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    # vat_catalog_check = models.BinaryField("входит ли в цену получаемую от поставщика" blank=True,
    #     null=True,)
    # last_catalog = document = models.FileField("Последний каталог", upload_to="get_file_path_add", null=True)
    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug_text = self.name
        slugish = translit.translify(slug_text)
        self.slug = slugify(slugish)

        super(Vendor, self).save(*args, **kwargs)


# class ListApiUploadIek(models.Model):
#     name = models.CharField("товары необходимые для загрузки апи иек", max_length=30)



class SupplierCategoryProduct(models.Model):
    name = models.CharField("Название категории", max_length=150)
    supplier = models.ForeignKey(
        Supplier,
        verbose_name="Поставщик",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    vendor = models.ForeignKey(
        Vendor,
        verbose_name="Вендор",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    article_name = models.CharField(
        "Артикул категории",
        max_length=25,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория товара у поставщика"
        verbose_name_plural = "Категории товаров у поставщика"

    def __str__(self):
        return f"{self.article_name}{self.name}"

    

class SupplierGroupProduct(models.Model):
    name = models.CharField("Название группы", max_length=150)
    slug = models.CharField("слаг", max_length=150,blank=True,
        null=True,)
    supplier = models.ForeignKey(
        Supplier,
        verbose_name="Поставщик",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        # !!!удалить нулы для вендоров
    )
    vendor = models.ForeignKey(
        Vendor,
        verbose_name="Вендор",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    article_name = models.CharField(
        "Артикул группы",
        max_length=25,
        blank=True,
        null=True,
    )
    category_supplier = models.ForeignKey(
        SupplierCategoryProduct,
        verbose_name="категория",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = "Группа товара у поставщика"
        verbose_name_plural = "Группы товаров у поставщика"

    def __str__(self):
        return self.name


class SupplierCategoryProductAll(models.Model):
    name = models.CharField("Название категории", max_length=150)
    slug = models.CharField("слаг", max_length=150,blank=True,
        null=True,)
    article_name = models.CharField(
        "Артикул категории",
        max_length=55,
        blank=True,
        null=True,
    )
    supplier = models.ForeignKey(
        Supplier,
        verbose_name="Поставщик",
        on_delete=models.PROTECT,
    )
    vendor = models.ForeignKey(
        Vendor,
        verbose_name="Вендор",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    category_supplier = models.ForeignKey(
        SupplierCategoryProduct,
        verbose_name="Категория каталога поставщика",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    group_supplier = models.ForeignKey(
        SupplierGroupProduct,
        verbose_name="Группа каталога поставщика",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    category_catalog = models.ForeignKey(
        "product.CategoryProduct",
        verbose_name="Категория каталога мотрум",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    group_catalog = models.ForeignKey(
        "product.GroupProduct",
        verbose_name="Группа каталога мотрум",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


    class Meta:
        verbose_name = "Подгруппы поставщиков"
        verbose_name_plural = "Подгруппы поставщиков"

    def __str__(self):
     
        return f"{self.name} {self.article_name}| Поставщик:{self.supplier} Вендор:{self.vendor}"
# {self.article_name}| Поставщик:{self.supplier} Вендор:{self.vendor}
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)         
        from apps.product.models import Price
        from apps.product.models import Product
        from apps.core.utils import get_category
        # обновление цен товаров связанной группы
        price = Price.objects.filter(prod__category_supplier_all=self.id)
        for price_one in price:
            price_one.price_supplier = price_one.price_supplier
            price_one.save()
           
            
       
       


class Discount(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        verbose_name="Поставщик",
        on_delete=models.PROTECT,
    )
    vendor = models.ForeignKey(
        Vendor,
        verbose_name="Производитель",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    # category_catalog = models.ForeignKey(
    #     "product.CategoryProduct",
    #     verbose_name="Категория каталога",
    #     on_delete=models.PROTECT,
    #     blank=True,
    #     null=True,
    # )

    # group_catalog = models.ForeignKey(
    #     "product.GroupProduct",
    #     verbose_name="Группа каталога",
    #     on_delete=models.PROTECT,
    #     blank=True,
    #     null=True,
    # )
    
    category_supplier = models.ForeignKey(
        SupplierCategoryProduct,
        verbose_name="Категория каталога поставщика",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    group_supplier = models.ForeignKey(
        SupplierGroupProduct,
        verbose_name="Группа каталога поставщика",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    category_supplier_all = models.ForeignKey(
        "SupplierCategoryProductAll",
        verbose_name="Приходящая категории товара от поставщиков",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    percent = models.FloatField("процент скидки")

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
        
    def __str__(self):
        return f"Скидка {self.vendor}|{self.vendor}:{self.percent}%"

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)         
        from apps.product.models import Price
        # обновление цен товаров связанной группы
        if self.category_supplier_all:
            print(11111)
            price = Price.objects.filter(prod__category_supplier_all=self.category_supplier_all)
        elif  self.group_supplier:
            price = Price.objects.filter(prod__group_supplier=self.group_supplier)
        elif  self.category_supplier:
            price = Price.objects.filter(prod__category_supplier=self.category_supplier) 
        elif  self.vendor:
            price = Price.objects.filter(prod__vendor=self.vendor)
        elif  self.supplier:
            price = Price.objects.filter(prod__supplier=self.supplier)              
        
        print(price)  
        for price_one in price:
            # price_one.price_supplier = price_one.price_supplier
            price_one.save()
            
