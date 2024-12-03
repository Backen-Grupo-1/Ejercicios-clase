from rest_framework import serializers
from biblioteca.models import Libro, Revista

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class RevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revista
        fields = '__all__'