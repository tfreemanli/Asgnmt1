from TWRL.models import Reservation
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Reservation)
def create_reservation(sender, instance, created, **kwargs):
    if created:
        print(f"Signal triggered: Reservation '{instance.title}' has been created.")
    else:
        print(f"Signal triggered: Reservation '{instance.title}' has been updated.")