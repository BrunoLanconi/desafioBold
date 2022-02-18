from rest_framework import viewsets, generics
from .models.sample import Sample
from .serializer import SamplesSerializer
from django.core.exceptions import ValidationError
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class SamplesViewSet(viewsets.ModelViewSet):  # all-in-one request method treatment (GET, POST, PUT, UPDATE)
    """
    Shows all samples
    """
    queryset = Sample.objects.all()  # what will be returned
    serializer_class = SamplesSerializer  # who will serialize returned content
    #authentication_classes = [BasicAuthentication]  # authentication method
    #permission_classes = [IsAuthenticated]  # authentication verification method


# Filters

class FilterSamplesList(generics.ListAPIView):
    """
    Shows all samples based on key and value
    """
    def get_queryset(self):
        try:
            queryset = Sample.objects.filter(**{self.kwargs["key"]: self.kwargs["value"]})

        except ValidationError:
            queryset = Sample.objects.none()

        return queryset
    serializer_class = SamplesSerializer
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
