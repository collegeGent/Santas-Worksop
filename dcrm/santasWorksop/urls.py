from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name=""),
    path("shop", views.shop, name="shop"),
]
