from django.urls import path
from .views import Items, Cakes, Product

urlpatterns =[
    path('cake/category/<str:category>/', Cakes),
    path('cake/cakecategoryIdentifier/<str:cakecategoryIdentifier>/', Items, name='items-list'),
    path('details/<str:name>', Product), 
]
