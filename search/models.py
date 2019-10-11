from django.db import models

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=100)
    frequency = models.BigIntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return f"name : {self.word}"