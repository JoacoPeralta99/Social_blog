from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models.signals import post_save
from simple_history.models import HistoricalRecords

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(default='batman.png')
    historical = HistoricalRecords()

    def __str__(self):
        return f'perfil de {self.user.username}'
    
class Post(models.Model):
    user = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'
    