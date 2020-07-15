from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.name}"