"""Models used to store tickets."""
from django.conf import settings
from django.db import models

STATUSES = (('I', 'Initial'),
            ('A', 'Awaiting Update'),
            ('F', 'Fixed'),
            ('W', 'Won\'t Fix'))

PRIORITIES = (('L', 'Low'),
              ('M', 'Medium'),
              ('H', 'High'))


class Ticket(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    attachment = models.FileField(upload_to='bugtracker', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUSES)
    priority = models.CharField(max_length=1, choices=PRIORITIES)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')

    class Meta:
        ordering = ['-updated_time']

    def __unicode__(self):
        return self.title


class TicketUpdate(models.Model):
    ticket = models.ForeignKey(Ticket)
    title = models.CharField(max_length=250)
    update_text = models.TextField()
    attachment = models.FileField(upload_to='bugtracker', blank=True, null=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')

    class Meta:
        ordering = ['-updated_time']

    def __unicode__(self):
        return '%s-update-%s' % (self.ticket.title, self.ticket.id)
