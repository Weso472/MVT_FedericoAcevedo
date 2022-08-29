from django.urls import path
from app_familiares.views import probar_template


urlpatterns = [
    path('', probar_template),
]