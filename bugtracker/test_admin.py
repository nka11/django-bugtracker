"""Monitoring Unit Test."""
from __future__ import absolute_import

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client
from django.views.decorators.csrf import csrf_exempt

from .models import Ticket, TicketUpdate


class SaveTicketTest(TestCase):
    """Save a ticket via the Admin."""

    @csrf_exempt
    def test_save_ticket(self):
        """Save a ticket"""
        self.user = get_user_model().objects.create_user('john',
                                                         'john@montypython.com',
                                                         'password')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.client = Client()
        self.client.login(username='john', password='password')

        response = self.client.post('/admin/bugtracker/ticket/add/',
                                    {'title': 'Test Ticket',
                                     'description': 'Created via Admin url',
                                     'status': 'I',
                                     'priority': 'L',
                                     'created_by': self.user.id,
                                     'assigned_to': self.user.id,
                                     'ticketupdate_set-0-attachment': '',
                                     'ticketupdate_set-__prefix__-update_text': '',
                                     'ticketupdate_set-INITIAL_FORMS': '0',
                                     'ticketupdate_set-0-ticket': '',
                                     'ticketupdate_set-0-update_text': 'Test Updated',
                                     'ticketupdate_set-__prefix__-ticket': '',
                                     'ticketupdate_set-TOTAL_FORMS': '1',
                                     'ticketupdate_set-MAX_NUM_FORMS': '1000',
                                     'ticketupdate_set-0-id': '',
                                     'ticketupdate_set-__prefix__-id': '',
                                     'ticketupdate_set-__prefix__-attachment': '',
                                     })
        self.assertEqual(response.status_code,
                         302,
                         'Unexpected status code on add, got %s expected 302' %
                             (response.status_code))

        ticket = Ticket.objects.get(title='Test Ticket')
        ticket_unicode = ticket.__unicode__()
        self.assertEqual(ticket_unicode,
                         'Test Ticket',
                         'Unexpected Ticket __unicode__, got %s expected "Test Ticket"' %
                             (ticket_unicode))

        ticket_update = TicketUpdate.objects.get(update_text='Test Updated')
        ticket_update_unicode = ticket_update.__unicode__()
        self.assertEqual(ticket_update_unicode,
                         'Test Ticket-update-1',
                         'Unexpected TicketUpdate __unicode__, got %s expected "Test Ticket-update-1"' %
                             (ticket_update_unicode))
