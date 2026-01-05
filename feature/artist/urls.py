from django.urls import path
from . import controller

urlpatterns = [
    path("create/", controller.create_artist),
    path("update/", controller.update_artist),
    path("get/", controller.get_artist),
    path("get-all/", controller.get_all_artist),
    path("delete/", controller.delete_artist),
]
