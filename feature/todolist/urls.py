from django.urls import path
from . import controller

urlpatterns = [
    path('create/', controller.create_api),   # POST
    path('update/', controller.update_api),   # PUT
    path('get/', controller.get_api),         # GET (single)
    path('all/', controller.get_all_api),     # GET (all)
    path('delete/', controller.delete_api),   # DELETE
]
