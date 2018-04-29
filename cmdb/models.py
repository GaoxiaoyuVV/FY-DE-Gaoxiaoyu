from django.db import models

# Create your models here.
class Show(models.Model):
    name=models.CharField(max_length=1000)
    description = models.TextField(max_length=10000,default='')
    example = models.TextField(max_length=10000, default='')
    hit=models.IntegerField(max_length=10000)
    #def __str__(self):
     #   return self.name