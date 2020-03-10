from django.db import models

from core.models import BaseModel
from update_request.constants import EnumUpdateRequestStatus


class UpdateRequest(BaseModel):
    REQUEST_STATUS = (
        (EnumUpdateRequestStatus.pending, "Pendente"),
        (EnumUpdateRequestStatus.cancelled, "Cancelado"),
        (EnumUpdateRequestStatus.finished, "Finalizado"),
    )

    project = models.ForeignKey("enviroinment.Project", on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=128)
    tickets = models.ManyToManyField("update_request.BugTrackerTicket")
    status = models.IntegerField(choices=REQUEST_STATUS, default=EnumUpdateRequestStatus.pending)


class BugTrackerTicket(BaseModel):
    ticket_number = models.CharField(max_length=64)
