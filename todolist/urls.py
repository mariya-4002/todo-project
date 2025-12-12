from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_todo),
    path("all/", views.get_all_todos),
    path("<int:id>/", views.get_todo),
    path("update/<int:id>/", views.update_todo),
    path("delete/<int:id>/", views.delete_todo),
]
