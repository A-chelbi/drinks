# Here we create all of the end points
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinksSerializer


def drink_list(request):
    # Get all the drinks
    # serialize them
    # return json
    drinks = Drink.objects.all()
    serializer = DrinksSerializer(drinks, many=True)
    return JsonResponse({'drinks': serializer.data})
