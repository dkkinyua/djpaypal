from django.db import models
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title
    

