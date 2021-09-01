from django.db import models


# Create your models here.
class ModeloEjemplo(models.Model):
    id1 = models.CharField(max_length=50)
    id2 = models.CharField(max_length=50)
    # rut = models.CharField(primary_key=True)

class ModeloNoBase():
    campo1=0
    campo2=''
