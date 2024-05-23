from django.shortcuts import render
from django.views.generic import View, TemplateView

from .models import Category


class MainPageView(TemplateView):
    template_name = 'main_page.html'

    def get_categories(self):
        categories_subcategories = {category: category.subcategories.all() for category in Category.objects.all()}
        return categories_subcategories

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories_subcategories"] = self.get_categories()
        return context
