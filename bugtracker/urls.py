from django.conf.urls import patterns, include, url
from bugtracker.models import Ticket
from views import TicketList

urlpatterns = patterns('',
    (r'^tickets/$', TicketList.as_view()),
)
