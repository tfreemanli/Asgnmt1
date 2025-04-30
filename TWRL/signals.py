from TWRL.models import Reservation
from django.db.models.signals import post_save
from django.dispatch import receiver
from postmarker.core import PostmarkClient
from Task2.settings import POSTMARK_API_TOKEN

@receiver(post_save, sender=Reservation)
def create_reservation(sender, instance, created, **kwargs):
    postmark = PostmarkClient(server_token=POSTMARK_API_TOKEN)
    if created:
        try:
            postmark.emails.send(
                From='lic96@myunitec.ac.nz',
                To=instance.client.email,
                Subject='Reservation Confirmation',
                HtmlBody=f'<html><body><p><strong>Thank you</strong></p><p>For your reservation of room {instance.room} from {instance.check_in_datetime} to {instance.check_out_datetime}.</p></body></html>'
            )
            print(f"Email Signal triggered :'{instance.client}' '{instance.client.email}'")
            print(f"Reservation '{instance.title}' room '{instance.room}' from '{instance.check_in_datetime}' to '{instance.check_out_datetime}' has been created.")

        except Exception as e:
            print(f"Error sending Create email: {e}")
    else:
        try:
            postmark.emails.send(
                From='lic96@myunitec.ac.nz',
                To=instance.client.email,
                Subject='Reservation Updated',
                HtmlBody=f'<html><body><p><strong>Successfully Updated</strong></p><p>your reservation of room {instance.room} from {instance.check_in_datetime} to {instance.check_out_datetime}.</p></body></html>'
            )
            print(f"Email Signal triggered :'{instance.client}' '{instance.client.email}'")
            print(f"Reservation '{instance.title}' room '{instance.room}' from '{instance.check_in_datetime}' to '{instance.check_out_datetime}' has been created.")

        except Exception as e:
            print(f"Error sending Update email: {e}")