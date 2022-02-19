from rest_framework import viewsets, generics
from .models.episode import Episode
from .models.genre import Genre
from .models.release import TitleRelease, EpisodeRelease
from .models.season import Season
from .models.title import Title
from .serializer import EpisodesSerializer, GenresSerializer, TitleReleasesSerializer, EpisodeReleasesSerializer, \
    SeasonsSerializer, TitlesSerializer
from django.core.exceptions import ValidationError


# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated


class EpisodesViewSet(viewsets.ModelViewSet):  # all-in-one request method treatment (GET, POST, PUT, UPDATE)
    """
    Shows all episodes
    """
    queryset = Episode.objects.all()  # what will be returned
    serializer_class = EpisodesSerializer  # who will serialize returned content
    # authentication_classes = [BasicAuthentication]  # authentication method
    # permission_classes = [IsAuthenticated]  # authentication verification method


class GenresViewSet(viewsets.ModelViewSet):
    """
    Shows all genres
    """
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class TitleReleasesViewSet(viewsets.ModelViewSet):
    """
    Shows all title releases
    """
    queryset = TitleRelease.objects.all()
    serializer_class = TitleReleasesSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class EpisodeReleasesViewSet(viewsets.ModelViewSet):
    """
    Shows all episode releases
    """
    queryset = EpisodeRelease.objects.all()
    serializer_class = EpisodeReleasesSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class SeasonsViewSet(viewsets.ModelViewSet):
    """
    Shows all seasons
    """
    queryset = Season.objects.all()
    serializer_class = SeasonsSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class TitlesViewSet(viewsets.ModelViewSet):
    """
    Shows all titles
    """
    queryset = Title.objects.all()
    serializer_class = TitlesSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


# Filters

class FilterEpisodesList(generics.ListAPIView):
    """
    Shows all episodes based on key and value
    """

    def get_queryset(self):
        try:
            queryset = Episode.objects.filter(**{self.kwargs["key"]: self.kwargs["value"]})

        except ValidationError:
            queryset = Episode.objects.none()

        return queryset

    serializer_class = EpisodesSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class FilterSeasonsList(generics.ListAPIView):
    """
    Shows all seasons based on key and value
    """

    def get_queryset(self):
        try:
            queryset = Season.objects.filter(**{self.kwargs["key"]: self.kwargs["value"]})

        except ValidationError:
            queryset = Season.objects.none()

        return queryset

    serializer_class = SeasonsSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class FilterTitlesList(generics.ListAPIView):
    """
    Shows all titles based on key and value
    """

    def get_queryset(self):
        try:
            queryset = Title.objects.filter(**{self.kwargs["key"]: self.kwargs["value"]})

        except ValidationError:
            queryset = Title.objects.none()

        return queryset

    serializer_class = TitlesSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
