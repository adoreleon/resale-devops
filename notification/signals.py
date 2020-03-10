from django.db.models.signals import post_save
from django.dispatch import receiver

from update_request.models import UpdateRequest


@receiver(post_save, sender=UpdateRequest)
def slack_handler(sender, **kwargs):
    pass
