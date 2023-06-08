from django.urls import path
from .views import *

urlpatterns = [
    path('', start, name='home'),
    path('<str:nav>/', page_detail_view, name='page'),
]
