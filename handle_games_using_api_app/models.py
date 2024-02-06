from django.db import models


class GamesSet(models.Model):
    name=models.CharField(max_length=50)
    creator=models.CharField(max_length=50)
    player=models.CharField(max_length=50)
    subscriber=models.CharField(max_length=50)