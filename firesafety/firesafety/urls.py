# firesafety/urls.py

from django.contrib import admin
from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add your URL patterns using views from the mainapp
]
