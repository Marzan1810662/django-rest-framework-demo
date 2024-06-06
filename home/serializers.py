from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields= ['name', 'age']
        # exclude = ['name', 'age'] #exclude these field from serializing
        fields= '__all__'