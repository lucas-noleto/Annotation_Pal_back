from django.db import models
from model_utils import Choices



# Create your models here.
class Entity(models.Model):
    name = models.TextField(primary_key=True)
    TYPE = Choices('Anime','Livro','Filme','Série','Dorama','Documentário')
    type = models.CharField(choices=TYPE)

    
    

class Note(models.Model):
    title = models.TextField()
    date=models.DateField()
    text=models.TextField()
    entity = models.ForeignKey(Entity,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['date']    