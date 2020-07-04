from django.urls import path
from . import views as notification_views


urlpatterns = [
    path('', notification_views.Notification.as_view(), name='notification')
]
