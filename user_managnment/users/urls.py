from django.urls import path, include  # Import include here
from users.views import dashboard
from users.views import register

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),  # Include the auth URLs properly
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
]
