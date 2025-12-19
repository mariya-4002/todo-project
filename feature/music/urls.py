from django.urls import path
from . import controller

urlpatterns = [
    path('create/', controller.create_music),   # POST
    path('update/', controller.update_music),   # PUT
    path('get/', controller.get_music),         # GET (single)
    path('all/', controller.get_all_music),     # GET (all)
    path('delete/', controller.delete_music),   # DELETE
]
