
from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.mi_armario,
        name="mi_armario"
    ),
    path(
        "eliminar/",
        views.eliminar_foto,
        name="eliminar_foto"
    ),
]
