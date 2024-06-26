from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.name
        # return str(self.id)

    class Meta:
        verbose_name: 'Person'