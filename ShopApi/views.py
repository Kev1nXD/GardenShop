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
        key_words = self.request.GET.get('key_words')
        if subcategory_id:
            queryset = queryset.filter(sub_category_id=subcategory_id)
        elif category_id:
            queryset = queryset.filter(sub_category__category_id=category_id)
        if key_words:
            queryset = queryset.filter(name__icontains=key_words)

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
        key_words = self.request.GET.get('key_words')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        color_id = self.request.GET.get('color')
        manufacturer_id = self.request.GET.get('manufacturer')
        context['min_price'] = min_price
        context['max_price'] = max_price
        context['color'] = Color.objects.get(pk=color_id) if color_id else None
        context['manufacturer'] = Manufacturer.objects.get(pk=manufacturer_id) if manufacturer_id else None
        if subcategory_id:
            context['subcategory'] = SubCategory.objects.get(pk=subcategory_id)
        elif category_id:
            context['category'] = Category.objects.get(pk=category_id)
        if key_words:
            context['key_words'] = key_words
        # Передача всех доступных цветов и производителей в контекст
        context['colors'] = Color.objects.all()
        context['manufacturers'] = Manufacturer.objects.all()
        return context


class CartPageView(TemplateView):
    template_name = 'cart.html'

class RecomendationsPageView(View):

    def recommendation_algorithm(self, local_storage):
        reviewed_products = local_storage.get('reviewed_products', [])


    @staticmethod
    def create_product_html(products):
        pass

    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        recommended_products = self.recommendation_algorithm(data)
        products_html = self.create_product_html(recommended_products)
        return JsonResponse({'products': products_html})

class SaveReview(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        Product.objects.get(pk=pk).reviews.create(
            review=data['review'])
        Product.get(pk=pk).rate = rating + Product.get(pk=pk).rate if Product.get(pk=pk).rate else rating
