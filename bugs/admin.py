from django.contrib import admin
from bugs.models import Ticket


# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'status')
    search_fields = ('title', 'status', 'date_created')
    readonly_fields = ('date_created',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Ticket, TicketAdmin)
