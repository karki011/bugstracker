from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from account.models import Account
from bugs.models import Ticket
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def get_ticket_status(filterby):
    ticket_filter = Ticket.objects.filter(status=filterby)
    return ticket_filter


@login_required
def home(request):
    html = 'bugs/home.html'
    new_ticket = get_ticket_status('NEW')
    in_progress = get_ticket_status('IN PROGRESS')
    completed = get_ticket_status('DONE')
    invalid = get_ticket_status('INVALID')
    tickets = Ticket.objects.all()
    context = {
        'tickets': tickets,
        'new_ticket': new_ticket,
        'in_progress': in_progress,
        'completed': completed,
        'invalid': invalid,
    }
    return render(request, html, context)


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket


class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.info(self.request, f'You have updated the reported bug.')
        return super().form_valid(form)

    def test_func(self):
        ticket = self.get_object()  # get the ticket first
        if self.request.user.is_admin:
            messages.warning(self.request, f'You are about to editing reported bug.')
            return True
        if self.request.user == ticket.created_by:
            messages.warning(self.request, f'You are about to editing reported bug.')
            return True
        return False


class UserTicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'bugs/user_ticket.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        user = get_object_or_404(Account, username=self.kwargs.get('username'))
        return Ticket.objects.filter(created_by=user).order_by('date_created')


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, f'You have reported the bug.')
        return super().form_valid(form)


@login_required()
def ticket_assigned_to_me(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.user_assigned = request.user
    ticket.status = "IN PROGRESS"
    messages.success(request, f'You have assigned ticket to yourself.')
    ticket.save()
    return HttpResponseRedirect(reverse('ticketdetail', kwargs={'pk': pk}))


@login_required()
def returnticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.user_assigned = ticket.clean_fields()
    ticket.user_completed = ticket.clean_fields()
    ticket.status = "NEW"
    messages.warning(request, f'You have returned this ticket!')
    ticket.save()
    return HttpResponseRedirect(reverse('ticketdetail', kwargs={'pk': pk}))


@login_required()
def completeticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    # ticket.user_assigned = ticket.clean_fields()
    ticket.status = "DONE"
    ticket.user_completed = request.user
    messages.success(request, f'You have marked this ticket as completed!')
    ticket.save()
    return HttpResponseRedirect(reverse('ticketdetail', kwargs={'pk': pk}))


@login_required()
def invalidticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.status = "INVALID"
    ticket.user_assigned = request.user
    ticket.user_completed = request.user
    messages.warning(request, f'You have marked this ticket as invalid!')
    ticket.save()
    return HttpResponseRedirect(reverse('ticketdetail', kwargs={'pk': pk}))
