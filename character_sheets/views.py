from rest_framework import viewsets, generics
from .serializers import CharacterSheetSerializer
from .models import Character_Sheet

# Create your views here.

class CharacterSheetView(viewsets.ModelViewSet):
    serializer_class = CharacterSheetSerializer
    queryset = Character_Sheet.objects.all()

class CharacterSheetCreateView(generics.CreateAPIView):
    queryset = Character_Sheet.objects.all()
    serializer_class = CharacterSheetSerializer
    lookup_field = 'id'

class CharacterSheetDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character_Sheet.objects.all()
    serializer_class = CharacterSheetSerializer
    lookup_field = 'id'

class CharacterSheetUpdateView(generics.UpdateAPIView):
    queryset = Character_Sheet.objects.all()
    serializer_class = CharacterSheetSerializer
    lookup_field = 'id'