# Here we create all of the end points
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request):
    # Get all the drinks
    # serialize them
    # return json

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinksSerializer(drinks, many=True)
        return JsonResponse({'drinks': serializer.data})

    if request.method == 'POST':
        serializer = DrinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
