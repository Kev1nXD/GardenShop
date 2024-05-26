from django.urls import path, re_path
from .views import MainPageView, ProductPageView, CategoryPageView, CartPageView, RecomendationsPageView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path(r'product_page/<int:pk>/', ProductPageView.as_view(), name='product_page'),
    re_path(r'category/(?P<category_id>\d+)/(?P<subcategory_id>\d+)/$', CategoryPageView.as_view(), name='category_page'),
    re_path(r'category/(?P<category_id>\d+)/$', CategoryPageView.as_view(), name='category_page'),
    path(r'cart/', CartPageView.as_view(), name='cart_page'),
    path(r'recomendations/', RecomendationsPageView.as_view(), name='recomendations_page'),
    re_path('category/', CategoryPageView.as_view(), name='search_products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
