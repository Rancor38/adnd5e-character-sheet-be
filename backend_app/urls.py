from django.urls import path, include
from rest_framework import routers
from character_sheets import views
from character_sheets.views import CharacterSheetCreateView, CharacterSheetDeleteView
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'character_sheets', views.CharacterSheetView, 'character_sheet')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/character_sheets/', CharacterSheetCreateView.as_view(), name='character_sheets_create'),
    path('api/character_sheets/<int:pk>/', CharacterSheetDeleteView.as_view(), name='character_sheet_delete'),
]
