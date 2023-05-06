from django.db import models

class Character_Sheet(models.Model):
    name = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    level = models.PositiveIntegerField()
    strength = models.PositiveIntegerField()
    dexterity = models.PositiveIntegerField()
    constitution = models.PositiveIntegerField()
    intelligence = models.PositiveIntegerField()
    wisdom = models.PositiveIntegerField()
    charisma = models.PositiveIntegerField()
    equipment = models.CharField(max_length=255)
    spells = models.CharField(max_length=255)
    backstory = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.character_class}, {self.race}, level {self.level})"
