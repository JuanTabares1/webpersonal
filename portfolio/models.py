from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name = "Título")
    description = models.TextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen", upload_to="projects")
    link = models.URLField(null=True, blank=True, verbose_name = "Enlace al proyecto")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Ultima vez editado")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title