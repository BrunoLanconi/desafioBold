from rest_framework import serializers
from .models.title import Title


class TitlesSerializer(serializers.ModelSerializer):  # used to convert information
    class Meta:
        model = Title  # model name to be serialized
        fields = "__all__"  # field's model to be serialized && use '__all__' to show all fields
