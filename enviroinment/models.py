from django.db import models

from core.models import BaseModel


class Enviroinment(BaseModel):
    name = models.CharField(max_length=128, verbose_name="Nome do ambiente")
    ip = models.GenericIPAddressField()


class Project(BaseModel):
    name = models.CharField(max_length=128)
    enviroinment = models.ForeignKey(Enviroinment, on_delete=models.CASCADE)
    url = models.URLField()
