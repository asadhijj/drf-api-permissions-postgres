from rest_framework import serializers

from .models import cars, engine


class carsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cars
        fields = [
            "type",
            "car_model",
            "car_fuel",
            "car_size",
            "car_economy",
            "purchaser",
        ]

        # fields = "all"


class engineSerializer(serializers.ModelSerializer):
    class Meta:
        model = engine
        fields = "all"