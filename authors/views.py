from rest_framework.viewsets import ModelViewSet
from .models import Kid, Sleep
from .serializers import KidModelSerializer, SleepModelSerializer


class KidModelViewSet(ModelViewSet):
    queryset = Kid.objects.all()
    serializer_class = KidModelSerializer


class SleepModelViewSet(ModelViewSet):
    queryset = Sleep.objects.all()
    serializer_class = SleepModelSerializer
