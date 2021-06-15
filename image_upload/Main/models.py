from django.db import models

# Create your models here.


class ImageUpload(models.Model):
    source_image = models.ImageField()
    checkprint_image = models.ImageField()
