from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView, DetailView, ListView

from .models import Category, Color, Manufacturer, Product, Review, SubCategory

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.reviews.all().count() != 0:
            context['raitings'] = round((float(self.object.rate) / self.object.reviews.all().count()), 2)
        return context




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
        if key_words:
            print(key_words)
            queryset = queryset.filter(name__icontains=key_words)

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


class SaveReview(View):

    def post(self, request, *args, **kwargs):
        pk = self.request.POST.get("id")
        user_name = self.request.POST.get('user-name')
        rating = self.request.POST.get('rating')
        comment = self.request.POST.get('comment')
       
        if (user_name and rating and comment):
            product = Product.objects.get(pk=pk)
            Review.objects.create(product=product, customer_name=user_name, review=comment)
            product.rate = (float(rating) + float(product.rate)) if product.rate else float(rating)
            product.save()
            return redirect('product_page', pk=pk)


class Recomendations(View):
        @staticmethod
        def buid_products_html(products):
            html = ''
            for product in products:
                html += open('ShopApi/product_html.txt', 'r', encoding='utf-8').read() % (
                product.pk, product.pk, product.image.url, product.name, product.name, product.description,
                product.price, product.pk, product.name, product.price, product.image.url)
            return html

        def post(self, request, *args, **kwargs):
            products = Product.objects.filter(rate__gte=4).order_by('-rate')[:5]
            recommended_product = self.buid_products_html(products)
            return JsonResponse({'recommended_product': recommended_product})