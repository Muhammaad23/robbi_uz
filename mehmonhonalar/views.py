from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mehmonhonlar
from .serializers import MehmonhonlarSerializer

class MehmonhonlarView(APIView):
    def get(self, request):
        # Retrieve all hotels (Mehmonhonlar)
        mehmonhonarlar = Mehmonhonlar.objects.all()
        serializer = MehmonhonlarSerializer(mehmonhonarlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new hotel (Mehmonhonlar)
        serializer = MehmonhonlarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new hotel instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
