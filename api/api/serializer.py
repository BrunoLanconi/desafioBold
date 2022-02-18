from rest_framework import serializers
from .models.title import Title
from .models.season import Season
from .models.episode import Episode


class TitlesSerializer(serializers.ModelSerializer):  # used to convert information
    class Meta:
        model = Title  # model name to be serialized
        fields = "__all__"  # field's model to be serialized && use '__all__' to show all fields


class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"


class EpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"
