from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Event(models.Model):
    event_name = models.CharField(max_length=50, unique=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='organizer_name')
    event_date = models.DateTimeField()
    event_date_reg_close = models.DateTimeField()
    event_location = models.CharField(max_length=100)
    event_location_url = models.URLField(max_length=200)
    number_cars = models.IntegerField(default=1)
    feature_cars = models.BooleanField(default=False)
    number_feature_cars = models.IntegerField(default=0)
    event_description = models.TextField()
    attendee = models.ManyToManyField(User, related_name='attendee_name')

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.event_name

    def number_of_attendees(self):
        return self.attendee.count()


class Siteuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event_organizer = models.BooleanField(default=False)
    site_owner = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_siteuser(sender, instance, created, **kwargs):
        if created:
            Siteuser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_siteuser(sender, instance, **kwargs):
        instance.siteuser.save()
