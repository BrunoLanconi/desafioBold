from django.urls import path, include
from .views import EpisodesViewSet, GenresViewSet, LanguagesViewSet, SeasonsViewSet, TitlesViewSet
from .views import FilterEpisodesList, FilterSeasonsList, FilterTitlesList
from rest_framework import routers

router = routers.DefaultRouter()  # url manager
router.register("episodes", EpisodesViewSet, basename="episodes")  # url registering on url manager
router.register("genres", GenresViewSet, basename="genres")
router.register("languages", LanguagesViewSet, basename="languages")
router.register("seasons", SeasonsViewSet, basename="seasons")
router.register("titles", TitlesViewSet, basename="titles")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),  # adding all urls managed by url manager
    path("episodes/<str:key>/<str:value>/", FilterEpisodesList.as_view()),
    path("seasons/<str:key>/<str:value>/", FilterSeasonsList.as_view()),
    path("titles/<str:key>/<str:value>/", FilterTitlesList.as_view()),
]
