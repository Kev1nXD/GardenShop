from django.contrib import admin

from .models import Category, Review, SubCategory, Color, Size, Product, Manufacturer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fieldsets = (
        ('Назва', {'fields': ('name',)}),
    )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('name', 'category')
    fieldsets = (
        ('Назва', {'fields': ('name',)}),
        ('Категорія', {'fields': ('category',)})
    )


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fieldsets = (
        ('Колір', {'fields': ('name',)}),
    )


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('height', 'width', 'weight')
    list_filter = ('height', 'width', 'weight')
    fieldsets = (
        ('Висота', {'fields': ('height',)}),
        ('Ширина', {'fields': ('width',)}),
        ('Вага', {'fields': ('weight',)}),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fieldsets = (
        ('Виробник', {'fields': ('name',)}),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'review_number', 'price', 'discount', 'sub_category', 'image')
    list_filter = ('name', 'rate', 'review_number', 'price', 'discount', 'sub_category', 'image')
    fieldsets = (
        ('Назва', {'fields': ('name',)}),
        ('Опис', {'fields': ('description',)}),
        ('Ціна', {'fields': ('price',)}),
        ('Знижка', {'fields': ('discount',)}),
        ('Підкатегорія', {'fields': ('sub_category',)}),
        ('Картинка', {'fields': ('image',)}),
        ('Характеристики', {'fields': ('size',)}),
        ('Виробник', {'fields': ('manufacturer',)}),
        ('Колір', {'fields': ('color',)}),
        
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'review')

