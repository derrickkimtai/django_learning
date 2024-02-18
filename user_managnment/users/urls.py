from django.urls import path, include  # Import include here
from users.views import dashboard

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),  # Include the auth URLs properly
    path("dashboard/", dashboard, name="dashboard"),
]
