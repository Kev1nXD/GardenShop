from django.contrib import admin

from .models import Category, Review, SubCategory, Color, Size, Product, Manufacturer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fieldsets = (
        ('Назва', {'fields': ('name',)}),  # Corrected to be a tuple and fixed the key to 'fields'
    )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('name', 'category')
    fieldsets = (
        ('Назва', {'fields': ('name',)}),  # Corrected the key to 'fields'
        ('Категорія', {'fields': ('category',)})  # Corrected the key to 'fields'
    )

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fieldsets = (
        ('Колір', {'fields': ('name',)}),  # Corrected 'field' to 'fields'
    )

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('height', 'width', 'weight')
    list_filter = ('height', 'width', 'weight')
    fieldsets = (
        ('Висота', {'fields': ('height',)}),  # Corrected 'field' to 'fields'
        ('Ширина', {'fields': ('width',)}),  # Corrected 'field' to 'fields'
        ('Вага', {'fields': ('weight',)}),  # Corrected 'field' to 'fields'
    )

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fieldsets = (
        ('Виробник', {'fields': ('name',)}),  # Corrected 'field' to 'fields'
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'review_number', 'price', 'discount', 'sub_category', 'image')
    list_filter = ('name', 'rate', 'review_number', 'price', 'discount', 'sub_category', 'image')
    fieldsets = (
        ('Назва', {'fields': ('name',)}),  # Corrected 'field' to 'fields'
        ('Опис', {'fields': ('description',)}),  # Corrected 'field' to 'fields'
        ('Ціна', {'fields': ('price',)}),  # Corrected 'field' to 'fields'
        ('Знижка', {'fields': ('discount',)}),  # Corrected 'field' to 'fields'
        ('Підкатегорія', {'fields': ('sub_category',)}),  # Corrected 'field' to 'fields'
        ('Картинка', {'fields': ('image',)}),  # Corrected 'field' to 'fields'
        ('Характеристики', {'fields': ('size',)}),  # Corrected 'field' to 'fields'
        ('Виробник', {'fields': ('manufacturer',)}),  # Corrected 'field' to 'fields'
        ('Колір', {'fields': ('color',)}),  # Corrected 'field' to 'fields'
        
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'review')