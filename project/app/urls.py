from django.urls import path
from .views import index

urlpatterns = [
    path('user/<str:name>/<int:age>', index, name='home'),
    path('user/<str:name>', index, name='home'),
    path('user', index, name='home'),
]