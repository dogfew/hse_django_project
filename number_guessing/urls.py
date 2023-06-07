from django.urls import path
from .views import number_guessing_view

app_name = 'number_guessing'

urlpatterns = [
    path('', number_guessing_view, name='guess'),
]