from django.urls import path
from . import views

urlpatterns = [
    path('kilinika_sanatoriya/', views.KilinikaSanatoriyaListView.as_view(), name='kilinika_sanatoriya-list'),
]
