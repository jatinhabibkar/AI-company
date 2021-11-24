from rest_framework import serializers
from .models import File,Data

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'timestamp')

class DataSerializer(serializers.ModelSerializer):
    class Meta():
        model = Data
        fields = '__all__'
        
    