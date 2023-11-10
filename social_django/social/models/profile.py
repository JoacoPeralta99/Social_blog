from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords

class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=False, null=False)
    image = models.ImageField(default='batman.png')
    historical = HistoricalRecords()

    class Meta:
        verbose_name = ("Perfil")
        verbose_name_plural=("Perfiles")

    def __str__(self):
        return f'perfil de {self.user.username}'
    