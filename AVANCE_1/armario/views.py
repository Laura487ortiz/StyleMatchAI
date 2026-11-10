
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import FotoArmarioForm
from .models import FotoArmario


def mi_armario(request):
    formulario = FotoArmarioForm()

    if request.method == "POST":
        formulario = FotoArmarioForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            foto_anterior = FotoArmario.objects.first()

            formulario.save()

            if foto_anterior:
                foto_anterior.imagen.delete(save=False)
                foto_anterior.delete()

            messages.success(
                request,
                "Imagen guardada correctamente."
            )

            return redirect("mi_armario")

    foto = FotoArmario.objects.order_by("-id").first()

    return render(
        request,
        "armario/mi_armario.html",
        {
            "formulario": formulario,
            "foto": foto,
        }
    )


@require_POST
def eliminar_foto(request):
    foto = FotoArmario.objects.order_by("-id").first()

    if foto:
        foto.imagen.delete(save=False)
        foto.delete()

    messages.success(
        request,
        "La fotografía fue eliminada."
    )

    return redirect("mi_armario")
