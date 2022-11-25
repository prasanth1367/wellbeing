from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.TextField()

class Water_list(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    litres = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name} {self.id} {self.litres}"