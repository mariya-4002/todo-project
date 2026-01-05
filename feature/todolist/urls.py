from django.urls import path
from . import controller

urlpatterns = [
    path('create/', controller.create_todo),      # POST
    path('update/', controller.update_todo),      # PUT
    path('get/', controller.get_todo),             # GET
    path('get-all/', controller.get_all_todo),     # GET
    path('delete/', controller.delete_todo),       # DELETE
]
