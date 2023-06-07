from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', start, name='home'),
   # path('<int:pk>/', page_detail_view, name='page'),
    path('<str:nav>/', page_detail_view, name='page'),
]
#
# pages = ['about.html',
#          'beautiful.html',
#          'codes.html',
#          'distros.html',
#          'formulas.html',
#          'index.html',
#          'scam.html']
#
# for page in pages:
#     name = page.split('.')[0]
#     urlpatterns.append(
#         path(name, SimpleHandler(page), name=name)
#     )
#
# urlpatterns.append(
#     path('forms', get_contact, name='forms')
# )
#
# urlpatterns.append(
#     path('opinion', get_opinion, name='opinion')
# )
#
# urlpatterns.append(
#     path('interactive', interactive_controller, name='interactive')
# )