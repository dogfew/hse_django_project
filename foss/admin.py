from django.contrib import admin
from .models import Page, Person,  Opinion, Task

admin.site.register(Page)
admin.site.register(Person)
admin.site.register(Opinion)
admin.site.register(Task)