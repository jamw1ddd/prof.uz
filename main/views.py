from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Starter
from .serializers import StarterSerializer

@api_view(['GET'])  
def starter_view(request):
    starters = Starter.objects.all()
    serializer = StarterSerializer(starters, many=True)
    return Response(serializer.data)