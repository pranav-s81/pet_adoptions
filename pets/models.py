from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pets/', blank=True, null=True)

    def __str__(self):
        return self.name
