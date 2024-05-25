from django.contrib import admin

from .models import Category, SubCategory, Color, Size, Product


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
