
const archivoInput = document.getElementById("id_imagen");
const imagenPreview = document.getElementById("imagen-preview");
const previewVacio = document.getElementById("preview-vacio");
const estadoGuardado = document.getElementById("estado-guardado");
const botonGuardar = document.getElementById("boton-guardar");
const botonCambiar = document.getElementById("boton-cambiar");
const avisoPendiente = document.getElementById("aviso-pendiente");
const errorCliente = document.getElementById("error-cliente");
const zonaCarga = document.getElementById("zona-carga");

let urlTemporal = null;

// Mostrar fotografía al seleccionarla
archivoInput.addEventListener("change", () => {
  const archivo = archivoInput.files[0];

  if (!archivo) return;

  const tiposAceptados = ["image/jpeg", "image/png"];

  if (
    !tiposAceptados.includes(archivo.type) ||
    archivo.size > 10 * 1024 * 1024
  ) {
    errorCliente.textContent =
      "Selecciona un JPG o PNG de máximo 10 MB.";

    errorCliente.classList.remove("oculto");
    archivoInput.value = "";
    botonGuardar.disabled = true;
    return;
  }

  errorCliente.classList.add("oculto");

  if (urlTemporal) {
    URL.revokeObjectURL(urlTemporal);
  }

  urlTemporal = URL.createObjectURL(archivo);

  imagenPreview.src = urlTemporal;
  imagenPreview.classList.remove("oculto");

  previewVacio.classList.add("oculto");
  estadoGuardado.classList.add("oculto");

  botonGuardar.disabled = false;
  botonCambiar.classList.remove("oculto");
  avisoPendiente.classList.remove("oculto");
});

// Cambiar fotografía
botonCambiar.addEventListener("click", () => {
  archivoInput.click();
});

// Permitir arrastrar fotografías
["dragenter", "dragover"].forEach((evento) => {
  zonaCarga.addEventListener(evento, (e) => {
    e.preventDefault();
    zonaCarga.classList.add("arrastrando");
  });
});

["dragleave", "drop"].forEach((evento) => {
  zonaCarga.addEventListener(evento, (e) => {
    e.preventDefault();
    zonaCarga.classList.remove("arrastrando");
  });
});

zonaCarga.addEventListener("drop", (e) => {
  const archivo = e.dataTransfer.files[0];

  if (!archivo) return;

  const transferencia = new DataTransfer();
  transferencia.items.add(archivo);

  archivoInput.files = transferencia.files;

  archivoInput.dispatchEvent(
    new Event("change", { bubbles: true })
  );
});
