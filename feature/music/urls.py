from django.urls import path
from .control import (
    create_music,
    update_music,
    get_music,
    get_all_music,
    delete_music
)

urlpatterns = [
    path('create/', create_music),
    path('update/', update_music),      # ❌ removed <int:music_id>
    path('get/', get_music),            # ❌ removed <int:music_id>
    path('all/', get_all_music),
    path('delete/', delete_music),      # ❌ removed <int:music_id>
]
