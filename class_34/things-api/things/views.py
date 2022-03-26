from rest_framework import generics
from .serializer import ThingSerializer
from .models import Thing
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ThingList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


