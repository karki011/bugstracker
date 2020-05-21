from django.db import models
from django.utils import timezone
from account.models import Account
# from bugs_bugs.settings import AUTH_USER_MODEL


# Create your models here.
# Each ticket should have the following fields:
#
# Title Time /
# Date filed
# Description
# Name of user who filed ticket Status of ticket (New / In Progress / Done /
# Invalid) --> hint: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices (Links to an external
# site.)Links to an external site.
# Name of user assigned to ticket Name of user who completed the ticket


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
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Created')
    user_assigned = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Assigned')
    user_completed = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Completed')
    status = models.CharField(max_length=11, choices=STATUS_OF_TICKET_CHOICES, default=NEW)

    def __str__(self):
        return self.title
