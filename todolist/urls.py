from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.create_todo),
    path('all/', views.get_all_todos),
    path('<int:todo_id>/', views.get_todo),
    path('update/<int:todo_id>/', views.update_todo),
    path('delete/<int:todo_id>/', views.delete_todo),
]
