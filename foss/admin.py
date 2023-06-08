from django.contrib import admin
from .models import Page, Person, Opinion, Task, LatexFormula, CodeExample, SoftExample

admin.site.register(Page)
admin.site.register(Person)
admin.site.register(Opinion)
admin.site.register(Task)
admin.site.register(LatexFormula)
admin.site.register(CodeExample)
admin.site.register(SoftExample)