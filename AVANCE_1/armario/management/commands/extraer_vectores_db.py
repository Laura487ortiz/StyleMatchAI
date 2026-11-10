import os
from django.core.management.base import BaseCommand
from armario.models import FotoArmario
from django.core.files import File
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

class Command(BaseCommand):
    help = 'Procesa una carpeta local de imágenes, las registra en la BD y extrae sus vectores con Fashion-CLIP.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Cargando el modelo Fashion-CLIP..."))
        
        model_id = "patrickjohncyh/fashion-clip"
        model = CLIPModel.from_pretrained(model_id)
        processor = CLIPProcessor.from_pretrained(model_id)
        model.eval()

        # Ruta de la carpeta local con tus imágenes (puedes cambiarla si se llama distinto)
        ruta_carpeta = os.path.join(os.getcwd(), 'dataset_prendas')

        if not os.path.exists(ruta_carpeta):
            self.stdout.write(self.style.ERROR(f"[ERROR] No se encontró la carpeta en: {ruta_carpeta}"))
            return

        self.stdout.write(f"Buscando imágenes en: {ruta_carpeta}")

        procesadas = 0
        for root, dirs, files in os.walk(ruta_carpeta):
            for filename in files:
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_path = os.path.join(root, filename)
                    try:
                        # Verificar si la prenda ya existe en la base de datos por nombre de archivo
                        prenda, creado = FotoArmario.objects.get_or_create(
                            defaults={}
                        )
                        
                        # Si prefieres asociar la imagen directamente abriéndola:
                        with open(image_path, 'rb') as f:
                            # Comprobamos si ya existe una foto con un nombre similar para no duplicar
                            obj, created = FotoArmario.objects.get_or_create(
                                imagen=filename
                            )
                            if created:
                                with open(image_path, 'rb') as img_file:
                                    obj.imagen.save(filename, File(img_file), save=True)
                                prenda_actual = obj
                            else:
                                prenda_actual = obj

                        # Extraer características con Fashion-CLIP
                        image = Image.open(image_path).convert("RGB")
                        inputs = processor(images=image, return_tensors="pt")
                        
                        with torch.no_grad():
                            outputs = model.get_image_features(pixel_values=inputs["pixel_values"])
                            image_features = outputs.pooler_output if hasattr(outputs, "pooler_output") else outputs
                        
                        # Normalizar y convertir a lista
                        image_features = image_features / image_features.norm(p=2, dim=-1, keepdim=True)
                        vector_np = image_features.cpu().numpy().flatten().tolist()
                        
                        # Guardar el vector en el modelo
                        prenda_actual.vector_caracteristicas = str(vector_np)
                        prenda_actual.save()
                        
                        procesadas += 1
                        self.stdout.write(self.style.SUCCESS(f"[ÉXITO] Procesada y vectorizada: {filename} (ID {prenda_actual.id})"))
                        
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"[ERROR] Falló {filename}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"\n¡Proceso finalizado! Total de prendas procesadas y guardadas: {procesadas}"))
