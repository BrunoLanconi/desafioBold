from django.urls import path, include
from .views import EpisodesViewSet, GenresViewSet, SeasonsViewSet, TitlesViewSet
from .views import FilterEpisodesList, FilterGenresList, FilterSeasonsList, FilterTitlesList
from rest_framework import routers

router = routers.DefaultRouter()  # url manager
router.register("episodes", EpisodesViewSet, basename="episodes")
router.register("genres", GenresViewSet, basename="genres")
router.register("seasons", SeasonsViewSet, basename="seasons")
router.register("titles", TitlesViewSet, basename="titles")  # url registering on url manager


app_name = "api"

urlpatterns = [
    path("", include(router.urls)),  # adding all urls managed by url manager
    path("titles/<str:key>/<str:value>/", FilterTitlesList.as_view()),
    path("seasons/<str:key>/<str:value>/", FilterSeasonsList.as_view()),
    path("episodes/<str:key>/<str:value>/", FilterEpisodesList.as_view()),
    path("genres/<str:key>/<str:value>/", FilterGenresList.as_view()),
]
