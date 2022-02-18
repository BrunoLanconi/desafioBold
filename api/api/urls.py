from django.urls import path, include
from .views import TitlesViewSet, SeasonsViewSet, EpisodesViewSet
from .views import FilterTitlesList, FilterSeasonsList, FilterEpisodesList
from rest_framework import routers

router = routers.DefaultRouter()  # url manager
router.register("titles", TitlesViewSet, basename="titles")  # url registering on url manager
router.register("seasons", SeasonsViewSet, basename="seasons")
router.register("episodes", EpisodesViewSet, basename="episodes")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),  # adding all urls managed by url manager
    path("titles/<str:key>/<str:value>/", FilterTitlesList.as_view()),
    path("seasons/<str:key>/<str:value>/", FilterSeasonsList.as_view()),
    path("episodes/<str:key>/<str:value>/", FilterEpisodesList.as_view()),
]
