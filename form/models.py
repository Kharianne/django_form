from django.db import models
from .validators import validate_ico


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=True)
    ico = models.CharField(max_length=8, blank=False, validators=[validate_ico])
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.ico} - {self.name}"
