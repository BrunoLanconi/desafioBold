from rest_framework import serializers
from .models.episode import Episode
from .models.genre import Genre
from .models.language import Language
from .models.release import TitleRelease, EpisodeRelease
from .models.season import Season
from .models.title import Title


class TitleReleasesSerializer(serializers.ModelSerializer):  # used to convert information
    class Meta:
        model = TitleRelease  # model name to be serialized
        fields = "__all__"  # field's model to be serialized && use '__all__' to show all fields


class EpisodeReleasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeRelease
        fields = "__all__"


class EpisodesSerializer(serializers.ModelSerializer):
    released = EpisodeReleasesSerializer(read_only=True, many=True)  # nesting related serializers

    class Meta:
        model = Episode
        fields = ("imdb_id", "title", "episode_number", "runtime",
                  "plot", "released", "imdb_rating", "poster",
                  "episode_owner_title", "episode_owner_season")


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class SeasonsSerializer(serializers.ModelSerializer):
    episodes = EpisodesSerializer(read_only=True, many=True)

    class Meta:
        model = Season
        fields = ("id", "season_owner_title", "season_number", "episodes")


class TitlesSerializer(serializers.ModelSerializer):
    seasons = SeasonsSerializer(read_only=True, many=True)
    released = TitleReleasesSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(read_only=True, many=True, slug_field="name")
    languages = serializers.SlugRelatedField(read_only=True, many=True, slug_field="name")

    class Meta:
        model = Title
        fields = ("imdb_id", "title", "genres", "plot", "languages",
                  "released", "imdb_rating", "poster", "seasons",
                  "created", "updated")
