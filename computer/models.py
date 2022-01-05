from django.db import models

#class computerManager(models.Manager):
   # def create(self):
    #    comp= self.create()
   #     comp.name='test'
     #   comp.nam='test'
      #  comp.save()
     #   return comp

class Basket(models.Model):
     name = models.CharField(max_length=200)
     description = models.CharField(max_length=200)
     price= models.CharField(max_length=20)
     pub_date= models.DateTimeField('date published')
     
class computer(models.Model):
     name = models.CharField(max_length=200)
     description = models.CharField(max_length=200)
     price= models.CharField(max_length=20)
     tip=models.DecimalField(max_digits=2, decimal_places=0)
     image =models.ImageField(upload_to='computer/%Y/%m/%d', blank=True)
     pub_date= models.DateTimeField('date published')
   #  object = computerManager()        
# Create your models here.
