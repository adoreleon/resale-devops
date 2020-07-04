from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView

from .forms import *
from notification.slack.business import SlackNotification
from .constants import EnumUpdateRequestStatus


class UpdateRequestListView(ListView):
    model = UpdateRequest
    queryset = UpdateRequest.objects.all()


def register_request(request):
    form = UpdateForm()
    if request.method == "POST":
        SlackNotification(request).process_signal("created", EnumUpdateRequestStatus.pending)
        # form.save()
        return HttpResponseRedirect("/updaterequest")
    return render(request, "register_request.html", {'form': form})
