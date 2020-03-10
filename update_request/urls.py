from django.urls import path
from update_request import views as update_request_views


urlpatterns = [
    path('', update_request_views.UpdateRequestListView.as_view(), name="update_request_list"),
]
