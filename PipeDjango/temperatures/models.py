from django.db import models
import uuid

class Temperature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.IntegerField(verbose_name='Temperatura(Centigrados)')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
