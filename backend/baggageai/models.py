from django.db import models

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)

class Data(models.Model):
  image_name = models.CharField(max_length=100)
  object_detected = models.CharField(max_length=200)
  timestamp = models.DateField()
