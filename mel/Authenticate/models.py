from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phoneNumber=models.IntegerField(max_length=12)
    description=models.TextField()
    def __str__(self) :
        return f'Message from {self.name}'