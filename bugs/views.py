from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from account.models import Account
from bugs.models import Ticket


# Create your views here.


def home(request):
    html = 'bugs/home.html'
    tickets = Ticket.objects.all()
    context = {
        'tickets': tickets
    }
    return render(request, html, context)


class TicketDetailView(DetailView):
    model = Ticket


class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Ticket
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ticket = self.get_object()  # get the ticket first
        if self.request.user.is_admin:
            return True
        if self.request.user == ticket.created_by:
            return True
        return False


class UserTicketListView(ListView):
    model = Ticket
    template_name = 'bugs/user_ticket.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        user = get_object_or_404(Account, username=self.kwargs.get('username'))
        return Ticket.objects.filter(created_by=user).order_by('-date_created')


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


def ticket_assigned_to_me(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.user_assigned = request.user
    ticket.save()
    return HttpResponseRedirect(reverse('ticketdetail', kwargs={'pk': pk}))
