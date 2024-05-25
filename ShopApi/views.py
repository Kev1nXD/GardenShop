from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView

from .models import Category, Product


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

