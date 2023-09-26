from django.db import models

class Game:
    secret_number = models.IntegerField()
    attempts = models.IntegerField(default=5)
    is_guessed = models.BooleanField(default=False)
    


# Create your models here.
