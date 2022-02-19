from rest_framework import serializers
from .models.episode import Episode
from .models.genre import Genre
from .models.season import Season
from .models.title import Title


class EpisodesSerializer(serializers.ModelSerializer):  # used to convert information
    class Meta:
        model = Episode  # model name to be serialized
        fields = "__all__"  # field's model to be serialized && use '__all__' to show all fields


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class SeasonsSerializer(serializers.ModelSerializer):
    episodes = EpisodesSerializer(read_only=True, many=True)  # nesting related serializers

    class Meta:
        model = Season
        fields = "__all__"


class TitlesSerializer(serializers.ModelSerializer):
    seasons = SeasonsSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(read_only=True, many=True, slug_field="name")

    class Meta:
        model = Title
        fields = "__all__"
