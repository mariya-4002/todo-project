from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apiapp.urls')),     # if you have apiapp for tests
    path('todo/', include('todolist.urls')),  # our new endpoints (base /todo/)
]
