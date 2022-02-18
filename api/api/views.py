from rest_framework import viewsets, generics
from .models.title import Title
from .models.season import Season
from .models.episode import Episode
from .serializer import TitlesSerializer, SeasonsSerializer, EpisodesSerializer
from django.core.exceptions import ValidationError
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TitlesViewSet(viewsets.ModelViewSet):  # all-in-one request method treatment (GET, POST, PUT, UPDATE)
    """
    Shows all titles
    """
    queryset = Title.objects.all()  # what will be returned
    serializer_class = TitlesSerializer  # who will serialize returned content
    # authentication_classes = [BasicAuthentication]  # authentication method
    # permission_classes = [IsAuthenticated]  # authentication verification method


class SeasonsViewSet(viewsets.ModelViewSet):
    """
    Shows all seasons
    """
    queryset = Season.objects.all()
    serializer_class = SeasonsSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class EpisodesViewSet(viewsets.ModelViewSet):
    """
    Shows all episodes
    """
    queryset = Episode.objects.all()
    serializer_class = EpisodesSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


# Filters

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
