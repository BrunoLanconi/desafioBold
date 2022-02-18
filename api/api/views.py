from rest_framework import viewsets, generics
from .models.title import Title
from .serializer import TitlesSerializer
from django.core.exceptions import ValidationError
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TitlesViewSet(viewsets.ModelViewSet):  # all-in-one request method treatment (GET, POST, PUT, UPDATE)
    """
    Shows all titles
    """
    queryset = Title.objects.all()  # what will be returned
    serializer_class = TitlesSerializer  # who will serialize returned content
    #authentication_classes = [BasicAuthentication]  # authentication method
    #permission_classes = [IsAuthenticated]  # authentication verification method


# Filters

class FilterSamplesList(generics.ListAPIView):
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
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
