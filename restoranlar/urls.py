from django.urls import path
from .views import RestoranlarListCreateView, RestoranMalumotlariView, MenuView


urlpatterns = [
    path('restoranlar/', RestoranlarListCreateView.as_view(), name='restoranlar-list-create'),
    path('restoran/', RestoranMalumotlariView.as_view(), name='restoran-list-create'),
    path('menu/', MenuView.as_view(), name='menu-list-create'),

]
