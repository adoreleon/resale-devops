from django.shortcuts import render, HttpResponseRedirect
from django.views import View


class Notification(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect("/")

