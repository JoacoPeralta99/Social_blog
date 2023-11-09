from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural=("Categorias")


    def __str__(self):
        return self.name
    
    