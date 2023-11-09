from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Opcional, si deseas vincular el autor a un usuario registrado.
    content = models.TextField(blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
   


    class Meta:
        verbose_name = ("Comentario")
        verbose_name_plural = ("Comentarios")


    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
    

    