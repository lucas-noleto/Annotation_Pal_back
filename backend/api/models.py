from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType




# Create your models here.
class Entity(models.Model):
    ENTITY_TYPE_CHOICES = [
        ('anime', 'Anime'),
        ('serie', 'Série'),
        ('filme', 'Filme'),
        ('dorama', 'Dorama'),
    ]

    GENRE_CHOICES = [
        ('ação', 'Ação'),
        ('romance', 'Romance'),
        ('comédia', 'Comédia'),
        ('histórico', 'Histórico'),
        ('policial', 'Policial'),
        ('fantasia', 'Fantasia'),
        ('terror', 'Terror'),
        ('suspense', 'Suspense'),
        ('aventura', 'Aventura'),
        ('musical', 'Musical'),
        ('drama', 'Drama'),
        ('velho oeste', 'Velho Oeste'),
        ('ficção cientifica', 'Ficção Cientifica'),
        ('documentário', 'Documentário'),
        ('biografia', 'Biografia'),
        
    ]


    title = models.TextField(unique=True)
    type = models.CharField(max_length=10, choices=ENTITY_TYPE_CHOICES)
    year = models.IntegerField()
    genres = models.CharField(max_length=255)
    
    class Meta:
        abstract = True
    

class Animes(Entity):
    GENRE_CHOICES = [
        ('hentai', 'Hentai'),
        ('shojo', 'Shojo'),
        ('kodomomuke', 'Kodomomuke'),
        ('shonen', 'Shonen'),
        ('seinen', 'Seinen'),
        ('josei', 'Josei'),
        ('shounen AI', 'Shounen AI'),
        ('shoujo AI', 'Shoujo AI'),
        ('yaoi', 'Yaoi'),
        ('yuri', 'Yuri'),
        ('mecha', 'Mecha'),
        ('code gears', 'Code Gears'),
        ('harem', 'Harem'),
        ('ecchi', 'Ecchi'),
        ('harem', 'Harem'),
        ('Reverse Harem', 'Reverse Harem'),
        ('yokai', 'Yokai'),
        ('isekai', 'Isekai'),
        ('slice of life', 'Slice of Life'),
        ('iyashikei', 'Iyashikei'),
        ('idol', 'Idol'),

        
    ]

    genres = models.CharField(max_length=255, choices=GENRE_CHOICES)

class Doramas(Entity):
    GENRE_CHOICES = [
        ('escolar', 'Escolar'),
        ('romance', 'Romance'),
        ('comédia', 'Comédia'),
        ('histórico', 'Histórico'),
        ('policial', 'Policial'),
        ('fantasia', 'Fantasia'),
        ('terror', 'Terror'),
        ('médico', 'Médico'),
    ]

    genres = models.CharField(max_length=255, choices=GENRE_CHOICES) 


class Filmes(Entity):
    pass

class Series(Entity):
    pass    
  
class Livros(Entity):     
    pass

class Note(models.Model):
    title = models.TextField()
    date=models.DateField()
    text=models.TextField()
    # user_id=
    object_id = models.PositiveIntegerField(null=True)
    content_type = models.ForeignKey(ContentType,null=True ,on_delete=models.CASCADE)
    entity = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        ordering = ['date']    
    
    def __str__(self):
        return self.title

    @property
    def entity_name(self):
        return self.entity.title