from django.shortcuts import render
from django.views.generic import ListView

from .forms import *


class UpdateRequestListView(ListView):
    model = UpdateRequest
    queryset = UpdateRequest.objects.all()


def register_request(request):
    form = UpdateForm()
    if request.method == "POST":
        return form.save()
    return render(request, "register_request.html", {'form': form})
