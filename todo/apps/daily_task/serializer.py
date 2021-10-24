from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    task = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=500)
    date = serializers.DateField()
