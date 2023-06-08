from django.contrib import admin
from .models import Page, Person, Opinion, Task, LatexFormula, CodeExample, SoftExample


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['title', 'nav_position', 'content']
    list_filter = ['nav_position']


admin.site.register(Person)
admin.site.register(Opinion)
admin.site.register(Task)
admin.site.register(LatexFormula)
@admin.register(CodeExample)
class CodeAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['header', 'code', 'lang']
    list_filter = ['lang']


admin.site.register(SoftExample)