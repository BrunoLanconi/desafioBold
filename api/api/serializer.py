from rest_framework import serializers
from .models.sample import Sample


class SamplesSerializer(serializers.ModelSerializer):  # used to convert information
    class Meta:
        model = Sample  # model name to be serialized
        fields = "__all__"  # field's model to be serialized && use '__all__' to show all fields
