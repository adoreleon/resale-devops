from django.contrib.auth.models import AnonymousUser
from django.db import models

from core.middleware import get_request


class BaseModel(models.Model):
    class Meta:
        abstract = True

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.updated_by = str(AnonymousUser)
        current_request = get_request()
        current_user = current_request.user

        if current_request.user is not None:
            self.updated_by = current_user

        return super(BaseModel, self).save(*args, **kwargs)
