from rest_framework import viewsets
from .models import *
from .serializers import *

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer 

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivroSerializer    

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Animes.objects.all()
    serializer_class = AnimeSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SerieSerializer

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filmes.objects.all()
    serializer_class = FilmeSerializer

class DoramaViewSet(viewsets.ModelViewSet):
    queryset = Doramas.objects.all()
    serializer_class = DoramaSerializer