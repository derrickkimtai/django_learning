from django.urls import path, include
from users.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]