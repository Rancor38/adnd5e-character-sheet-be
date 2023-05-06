from rest_framework import serializers
from .models import Character_Sheet

class CharacterSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character_Sheet
        fields = ('id', 'name', 'character_class', 'race', 'level', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'equipment', 'spells', 'backstory')