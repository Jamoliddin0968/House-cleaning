from django.db import models

STATUS_CHOICES = (
    (), (), ()
)


class Contact(models.Model):
    first_name = models.CharField(max_length=31)
    phone_number = models.CharField(max_length=13)
    # status = models.
