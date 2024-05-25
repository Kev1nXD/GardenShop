from django.contrib import admin

from .models import Category, SubCategory, Characteristic, Product


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


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('type', 'value')
    list_filter = ('type', 'value')
    fieldsets = (
        ('Тип', {'fields': ('type',)}),  # Fixed 'fileds' to 'fields'
        ('Значення', {'fields': ('value',)})  # Fixed 'fileds' to 'fields'
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
        ('Характеристики', {'fields': ('characteristics',)}),  # Corrected 'field' to 'fields'
    )
