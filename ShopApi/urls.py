from django.urls import path
from .views import (MainPageView, ProductPageView)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path("product_page/<int:pk>/", ProductPageView.as_view(), name='product_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
