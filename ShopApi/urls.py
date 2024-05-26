from django.urls import path, re_path
from .views import MainPageView, ProductPageView, CategoryPageView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('product_page/<int:pk>/', ProductPageView.as_view(), name='product_page'),
    re_path(r'category/(?P<category_id>\d+)/(?P<subcategory_id>\d+)/$', CategoryPageView.as_view(), name='category_page'),
    re_path(r'category/(?P<category_id>\d+)/$', CategoryPageView.as_view(), name='category_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
