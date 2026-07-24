from django.db import models

# Create your models here.

class Event(models.Model):


    img=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=50)
    description=models.TextField()
    location=models.CharField(max_length=100)
    event_date=models.DateField()
    event_time=models.TimeField()

    def __str__(self):
        return self.name
