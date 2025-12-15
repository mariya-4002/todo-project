from django.urls import path
from . import control

urlpatterns = [
    path('create/', control.create_api),   # POST
    path('update/', control.update_api),   # PUT
    path('get/', control.get_api),         # GET (single by id)
    path('all/', control.get_all_api),     # GET (all)
    path('delete/', control.delete_api),   # DELETE
]
