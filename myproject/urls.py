from django.contrib import admin
from django.urls import path, include

from feature.common.swagger import schema_view  # ✅ IMPORT HERE


urlpatterns = [
    path("admin/", admin.site.urls),

    # Features
    path("todolist/", include("feature.todolist.urls")),
    path("music/", include("feature.music.urls")),
    path("artist/", include("feature.artist.urls")),

    # Swagger URLs
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
