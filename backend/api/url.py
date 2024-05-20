from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import* 
from rest_framework import routers

    

router = DefaultRouter()
router.register(r'note', NoteViewSet, basename='note')
router.register(r'livro', LivroViewSet, basename='livro')
router.register(r'serie', SerieViewSet, basename='serie')
router.register(r'dorama', DoramaViewSet, basename='dorama')
router.register(r'anime', AnimeViewSet, basename='anime')
router.register(r'filme', FilmeViewSet, basename='filme')
 

# Create a router and register our ViewSets with it.

 

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]