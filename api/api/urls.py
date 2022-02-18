from django.urls import path, include
from .views import TitlesViewSet
from .views import FilterSamplesList
from rest_framework import routers

router = routers.DefaultRouter()  # url manager
router.register("titles", TitlesViewSet, basename="titles")  # url registering on url manager

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),  # adding all urls managed by url manager
    path("titles/<str:key>/<str:value>/", FilterSamplesList.as_view()),
]
