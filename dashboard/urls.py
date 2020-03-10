from django.urls import path
from dashboard import views as dash_views


urlpatterns = [
    path('', dash_views.dashboard_view, name="dashboard"),
]
