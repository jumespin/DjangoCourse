from django.db import models

# Create your models here.

class ProfesionDb(models.Model):
        nombre= models.CharField(verbose_name = "Profesión", max_length=75)

        def __str__(self) -> str:
             return self.nombre


class AutorDb(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    fecha_nacimiento = models.DateField(verbose_name = "Fecha Nacimiento", null=False, blank=False)
    fecha_fallecimiento = models.DateField(verbose_name = "Fecha Fallecimiento", null=True, blank=True)
    profesion = models.ManyToManyField(ProfesionDb, verbose_name="Profesion")
    nacionalidad = models.CharField(max_length=50, verbose_name="Nacionalidad")

    class Meta:
        db_table = "Autores" 
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self) -> str:
        return self.nombre

class FraseDb(models.Model):
    quote = models.TextField(verbose_name="Cita", max_length=500)
    autor_fk =models.ForeignKey(AutorDb, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"
