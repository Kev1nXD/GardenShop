from django.urls import path, re_path
<<<<<<< HEAD
from .views import MainPageView, ProductPageView, CategoryPageView
=======
from .views import MainPageView, ProductPageView, CategoryPageView, CartPageView
>>>>>>> 7bb3b2e6bebba61021555f09a5c46875067a0008
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('product_page/<int:pk>/', ProductPageView.as_view(), name='product_page'),
    re_path(r'category/(?P<category_id>\d+)/(?P<subcategory_id>\d+)/$', CategoryPageView.as_view(), name='category_page'),
    re_path(r'category/(?P<category_id>\d+)/$', CategoryPageView.as_view(), name='category_page'),
<<<<<<< HEAD
=======
    path('cart/', CartPageView.as_view(), name='cart_page'),
>>>>>>> 7bb3b2e6bebba61021555f09a5c46875067a0008
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
