from django.urls import path
from . import control

urlpatterns = [
    path('create/', control.create_api),
    path('update/<int:id>/', control.update_api),
    path('get/<int:id>/', control.get_api),
    path('all/', control.get_all_api),
    path('delete/<int:id>/', control.delete_api),
]
