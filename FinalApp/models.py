from django.db import models

# Create your models here.

class Game(models.Model):
    gameDeveloper=models.CharField(max_length=50, default="")
    gameName=models.CharField(max_length=70)
    gameGenre=models.CharField(max_length=30, default="")
    gameRelease=models.DateField()
    gameScore=models.FloatField()
    gameReview=models.TextField(max_length=300)


class upcomingGame(models.Model):
    upcomingName=models.CharField(max_length=70)
    upcomingRelease=models.DateField()
    upcomingsWallpaper=models.ImageField(upload_to = 'games', null=True)

