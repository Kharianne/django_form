from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'ico']
    ordering = ['created']

    def has_add_permission(self, request):
        return False

    """
    In case we want to restrict deletion or update of record,
    uncomment this section
    
    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    """