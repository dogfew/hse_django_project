from django.contrib import admin
from .models import Page, Person,  Opinion, Task

admin.site.register(Page)
admin.site.register(Person)
admin.site.register(Opinion)
admin.site.register(Task)
#
# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#     list_display = ['id', 'item_title', 'item_nav', 'item_nav_position', 'item_content', 'item_current_date']
#     list_display_links = ['item_title', ]
#     list_editable = ['item_nav', 'item_nav_position',]
#     search_fields = ['item_content',]
#     list_filter = ['item_title', 'item_nav']
#     list_per_page = 15