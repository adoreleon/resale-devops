from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=128)
