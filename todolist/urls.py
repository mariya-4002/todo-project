from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_todo),              # POST
    path('all/', views.get_all_todos),         # GET all
    path('<int:id>/', views.get_todo),         # GET one
    path('update/<int:id>/', views.update_todo),   # PUT
    path('delete/<int:id>/', views.delete_todo),   # DELETE
]
