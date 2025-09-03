from django.urls import path
from .views import SignUpView, dashboard

urlpatterns = [
   path('dashboard/', dashboard, name='dashboard'),
]