from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=800)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

