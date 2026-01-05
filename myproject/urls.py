from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('feature.todolist.urls')),
    path('music/', include('feature.music.urls')),
    path("artist/", include("feature.artist.urls")),

]
