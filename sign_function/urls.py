from django.urls import path
from .views import FilteredSignView

app_name = 'sign_function'

urlpatterns = [
    path('', FilteredSignView.as_view(), name='sign'),
]