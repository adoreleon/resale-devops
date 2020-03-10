from django.shortcuts import render
from django.views.generic import ListView

from update_request.models import UpdateRequest


class UpdateRequestListView(ListView):
    model = UpdateRequest
    queryset = UpdateRequest.objects.all()
