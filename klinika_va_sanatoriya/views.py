from rest_framework import generics
from .models import Kilinika_sanatoriya
from .serializers import KilinikaSanatoriyaSerializer

class KilinikaSanatoriyaListView(generics.ListAPIView):
    queryset = Kilinika_sanatoriya.objects.all()
    serializer_class = KilinikaSanatoriyaSerializer
