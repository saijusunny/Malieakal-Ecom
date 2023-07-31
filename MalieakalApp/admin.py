from django.contrib import admin
from .models import *

class ChildModelAdmin(admin.ModelAdmin):
    list_display = ('description', 'get_parent_name')

    def get_parent_name(self, obj):
        return obj.parent.name if obj.parent else None

    get_parent_name.admin_order_field = 'parent__name'  # Allow ordering by parent name
    get_parent_name.short_description = 'Parent Name'


admin.site.register(User_Registration)
admin.site.register(category)
admin.site.register(item,ChildModelAdmin)
admin.site.register(bannerads)
