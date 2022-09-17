from django.db import models

class Machine(models.Model):
    game = models.CharField(max_length=100);
    manufacturer = models.CharField(max_length=40);
    releaseYear = 	models.IntegerField();

    class Meta:
        ordering = ['game']

    def __str__(self):
        return self.game

class Location(models.Model):
    zip = models.CharField(max_length=100);
    state = models.CharField(max_length=2);
    buisness = 	models.CharField(max_length=100);
    address = models.CharField(max_length=200);
    machines = models.ManyToManyField(Machine);

    class Meta:
        ordering = ['zip']

    def __str__(self):
        return self.buisness 