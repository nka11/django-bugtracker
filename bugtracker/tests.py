"""Bugtracker Unit Test."""

from django.test import TestCase
from django.contrib.auth.models import User

from .models import STATUSES, PRIORITIES, Ticket, TicketUpdate


class CreateTicketTest(TestCase):
    """Create and Update a Ticket."""
    
    def test_create_and_update_ticket(self):
        """Create and update a ticket"""
        user = User.objects.create_user('john', 'john@montypython.com', 'password')
        user.save()
        ticket = Ticket.objects.create(title='Test Ticket',
                                       description='This is a test',
                                       status=STATUSES[0][0],
                                       priority=PRIORITIES[0][0],
                                       created_by=user,
                                       assigned_to=user)
        ticket.save()
        self.assertEqual(ticket.title, 
                         'Test Ticket',
                         'Unexpected ticket title, got "%s" expected "Test Ticket"' % 
                            (ticket.title))
        
        ticket_update = TicketUpdate.objects.create(ticket=ticket,
                                                    title='Test Ticket Update',
                                                    update_text='This is a test update',
                                                    updated_by=user)
        ticket_update.save()

        self.assertEqual(ticket_update.title, 
                         'Test Ticket Update',
                         'Unexpected ticket update title, got "%s" expected "Test Ticket Update"' % 
                            (ticket.title))