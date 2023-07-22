from django.db import models

class Snippet(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    secret_key = models.CharField(max_length=50, blank=True)
