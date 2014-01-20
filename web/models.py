from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .fields import CurrencyField


class VenueType(models.Model):
    type_text = models.CharField(max_length=16)


class Event(models.Model):
    name_text = models.CharField(max_length=128)
    description_text = models.CharField(max_length=2048)
    owner = models.ForeignKey(User)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    location_text = models.CharField(max_length=64)

    def get_absolute_url(self):
        return '/event/{}'.format(self.pk)


class EventType(models.Model):
    # There needs to be a check on both venue_type and event to ensure there are
    # no duplicates of these keys in the database
    venue_type = models.ForeignKey(VenueType)
    event = models.ForeignKey(Event)


class CostType(models.Model):
    type_text = models.CharField(max_length=64)


class EventCost(models.Model):
    # There needs to be a check on both cost_type and event to ensure there are
    # no duplicates of these keys in the database
    cost_type = models.ForeignKey(CostType)
    event = models.ForeignKey(Event)

    value = CurrencyField(help_text='The cost in US dollars')