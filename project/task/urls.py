from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    re_path(r'^user/(?P<login>\D+)/(?P<folder>\D+)/(?P<folder_num>\d+)', index),
    re_path(r'^user/(?P<login>\D+)/(?P<folder>\D+)', index),
    re_path(r'^user/(?P<login>\D+)/', index),
    re_path(r'^user/', index),
]