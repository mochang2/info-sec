from django.db import models

# Create your models here.


class Post(models.Model):
    # id : auto created field
    title = models.CharField(max_length=100)
    writer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
