from django.urls import path, include
from bugs.views import home, TicketCreateView, TicketDetailView, TicketUpdateView, UserTicketListView, \
    ticket_assigned_to_me, returnticket, completeticket, invalidticket

urlpatterns = [
    path('', home, name='home'),
    path('user/<str:username>/', UserTicketListView.as_view(), name="userticket"),
    path('ticket/new/', TicketCreateView.as_view(), name='ticketcreate'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name="ticketdetail"),
    path('ticket/<int:pk>/update/', TicketUpdateView.as_view(), name="ticketupdate"),
    path('ticket/assigntome/<int:pk>/', ticket_assigned_to_me, name='assigntome'),
    path('ticket/returnticket/<int:pk>/', returnticket, name='returnticket'),
    path('ticket/completed/<int:pk>/', completeticket, name='completedticket'),
    path('ticket/invalid/<int:pk>/', invalidticket, name='invalidticket'),

]
