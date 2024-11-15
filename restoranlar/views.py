from rest_framework import generics
from .models import Restoranlar
from .serializers import RestoranlarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restoran_malumotlari
from .serializers import RestoranMalumotlariSerializer
from .models import Menu
from .serializers import MenuSerializer


class RestoranlarListCreateView(generics.ListCreateAPIView):
    queryset = Restoranlar.objects.all()
    serializer_class = RestoranlarSerializer

class RestoranMalumotlariView(APIView):
    # Retrieve all instances
    def get(self, request):
        restoranlar = Restoran_malumotlari.objects.all()
        serializer = RestoranMalumotlariSerializer(restoranlar, many=True)
        return Response(serializer.data)


    # Create a new instance
    def post(self, request):
        serializer = RestoranMalumotlariSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuView(APIView):
    def get(self, request):
        # Retrieve all menu items
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new menu item
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)