from django.urls import path

from .views import *

urlpatterns = [
    path('', SimpleHandler('index.html'), name='home'),
]

pages = ['about.html',
      #   'opinion.html',
         'beautiful.html',
         'codes.html',
         'distros.html',
      #   'forms.html',
         'formulas.html',
         'index.html',
     #    'interactive.html',
         'scam.html']

for page in pages:
    name = page.split('.')[0]
    urlpatterns.append(
        path(name, SimpleHandler(page), name=name)
    )

urlpatterns.append(
    path('forms', get_contact, name='forms')
)

urlpatterns.append(
    path('opinion', get_opinion, name='opinion')
)

urlpatterns.append(
    path('interactive', interactive_controller, name='interactive')
)