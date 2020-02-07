from django.db import models

# Create your models here.
class destinationdemo(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.FileField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField()


