from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from music.models import Artist
from music.serializers import ArtistSerializer

# Create your views here.


def index(_request):
    return HttpResponse("My first API!")


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
