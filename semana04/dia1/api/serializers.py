from rest_framework import serializers

from .models import Profesor

class AlumnoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    
class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'