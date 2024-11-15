from django.urls import path
from .views import MehmonhonlarView

urlpatterns = [
    path('mehmonhonlar/', MehmonhonlarView.as_view(), name='mehmonhonlar-list'),  # List and create hotels
]
