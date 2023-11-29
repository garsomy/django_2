from django.urls import path, include
from .views import *

product_urls = [
    path('product', product, name='product'),
    path('cart', cart, name='cart'),
    path('order', order, name='order'),
]

urlpatterns = [
    path('', main, name='home'),
    path('news', news, name='news'),
    path('shop/<int:pk>/', include(product_urls)),
    path('faq', faq, name='faq'),
]