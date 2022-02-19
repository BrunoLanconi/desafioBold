from rest_framework import serializers
from .models.episode import Episode
from .models.genre import Genre
from .models.release import TitleRelease, EpisodeRelease
from .models.season import Season
from .models.title import Title


class TitleReleasesSerializer(serializers.ModelSerializer):  # used to convert information
    class Meta:
        model = TitleRelease  # model name to be serialized
        fields = ["day", "month", "year"]  # field's model to be serialized && use '__all__' to show all fields


class EpisodeReleasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeRelease
        fields = ["day", "month", "year"]


class EpisodesSerializer(serializers.ModelSerializer):
    episode_release = EpisodeReleasesSerializer(read_only=True, many=True)  # nesting related serializers

    class Meta:
        model = Episode
        fields = ["title", "plot", "runtime", "episode_release", "imdb_rating", "poster"]


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class SeasonsSerializer(serializers.ModelSerializer):
    episodes = EpisodesSerializer(read_only=True, many=True)

    class Meta:
        model = Season
        fields = ["season_number", "episodes"]


class TitlesSerializer(serializers.ModelSerializer):
    seasons = SeasonsSerializer(read_only=True, many=True)
    title_release = TitleReleasesSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(read_only=True, many=True, slug_field="name")

    class Meta:
        model = Title
        fields = ["title", "plot", "genres", "language", "title_release", "imdb_rating", "poster", "seasons"]
