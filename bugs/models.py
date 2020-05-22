from django.db import models
from django.utils import timezone
from account.models import Account
from django.shortcuts import reverse
from datetime import datetime

from bugs_bugs.settings import AUTH_USER_MODEL


class Ticket(models.Model):
    NEW = 'NEW'
    IN_PROGRESS = 'IN PROGRESS'
    DONE = 'DONE'
    INVALID = 'INVALID'
    STATUS_OF_TICKET_CHOICES = [
        (NEW, 'NEW'),
        (IN_PROGRESS, 'IN PROGRESS'),
        (DONE, 'DONE'),
        (INVALID, 'INVALID'),
    ]
    title = models.CharField(max_length=120)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Created', )
    user_assigned = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Assigned', blank=True,
                                      null=True)
    user_completed = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Completed',
                                       blank=True, null=True)
    status = models.CharField(max_length=11, choices=STATUS_OF_TICKET_CHOICES, default=NEW)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticketdetail', kwargs={'pk': self.pk})


