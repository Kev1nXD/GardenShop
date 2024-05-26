from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView, ListView

from .models import Category, Color, Manufacturer, Product, SubCategory

class MainPageView(TemplateView):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().prefetch_related('subcategory_set')
        return context

class ProductPageView(DetailView):
    template_name = 'product_page.html'
    model = Product
    context_object_name = 'product'

class CategoryPageView(ListView):
    template_name = 'category_page.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.kwargs.get('category_id')
        subcategory_id = self.kwargs.get('subcategory_id')
        if subcategory_id:
            queryset = queryset.filter(sub_category_id=subcategory_id)
        elif category_id:
            queryset = queryset.filter(sub_category__category_id=category_id)

        # Фильтрация по цвету
        color_id = self.request.GET.get('color')
        if color_id:
            queryset = queryset.filter(color_id=color_id)

        # Фильтрация по производителю
        manufacturer_id = self.request.GET.get('manufacturer')
        if manufacturer_id:
            queryset = queryset.filter(manufacturer_id=manufacturer_id)

        # Фильтрация по цене
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        subcategory_id = self.kwargs.get('subcategory_id')
        if subcategory_id:
            context['subcategory'] = SubCategory.objects.get(pk=subcategory_id)
        elif category_id:
            context['category'] = Category.objects.get(pk=category_id)

        # Передача всех доступных цветов и производителей в контекст
        context['colors'] = Color.objects.all()
        context['manufacturers'] = Manufacturer.objects.all()
        return context


class CartPageView(TemplateView):
    template_name = 'cart.html'