from rest_framework import serializers
from .models import Locaions

class LocaionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locaions
        fields = '__all__'