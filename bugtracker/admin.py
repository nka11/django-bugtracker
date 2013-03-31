from django.contrib import admin
from bugtracker.models import Ticket, TicketUpdate


class TicketUpdateInline(admin.TabularInline):
    model = TicketUpdate
    fields = ('update_text', 'attachment', 'updated_time', 'updated_by')
    readonly_fields = ('updated_time', 'updated_by')
    can_delete = False
    extra = 0


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority',
                    'created_by', 'created_time', 'updated_time')
    list_filter = ('status', 'priority', 'updated_time', 'assigned_to')
    search_fields = ('title', 'description',)
    readonly_fields = ('created_by', 'created_time', 'updated_time',)
    inlines = [TicketUpdateInline]
    fieldsets = (
        (None, {
            'fields': (('title',),
                       ('status', 'priority',),
                       ('created_by', 'created_time',),
                       ('assigned_to',),
                       ('description',),
                       ('attachment'),
                       )
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        if formset.model == TicketUpdate:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.updated_by = request.user
                instance.save()
        else:
            formset.save()

admin.site.register(Ticket, TicketAdmin)
