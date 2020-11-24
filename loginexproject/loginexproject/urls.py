from django.contrib import admin
from django.urls import path

import loginapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginapp.views.index, name='index'),
    path('result/', loginapp.views.result, name='result'),
]
