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

class CharacterSheetByUser(generics.ListAPIView):
    serializer_class = CharacterSheetSerializer

    def get_queryset(self):
        user_sub = self.kwargs['user_sub']
        return Character_Sheet.objects.filter(user_sub=user_sub)