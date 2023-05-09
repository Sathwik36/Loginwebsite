from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField( max_length=50)
    pno=models.CharField( max_length=10)
    email=models.CharField( max_length=50)
    desc=models.TextField()
    

    def __str__(self):
        return self.name
    