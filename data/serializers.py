from rest_framework import serializers
from .models import StudentData


class StudentApi(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    roll = serializers.CharField(max_length=200)

    def create(self, validate_data):
        return StudentData.objects.create(**validate_data)
