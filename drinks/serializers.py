# describing the process to going from a python object to json
from rest_framework import serializers
from .models import Drink


class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ["id", "name", "description"]
