from django.urls import path, include
from bugs.views import home, TicketCreateView, TicketDetailView, TicketUpdateView, UserTicketListView

urlpatterns = [
    path('', home, name='home'),
    path('user/<str:username>/', UserTicketListView.as_view(), name="userticket"),
    path('ticket/new/', TicketCreateView.as_view(), name='ticketcreate'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name="ticketdetail"),
    path('ticket/<int:pk>/update/', TicketUpdateView.as_view(), name="ticketupdate"),

]
