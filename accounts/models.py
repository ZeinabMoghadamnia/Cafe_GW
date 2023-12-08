from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    CUSTOMERUSER_EMPLOYEE = 'e'
    CUSTOMERUSER_CUSTOMER = 'c'
    CUSTOMERUSER_MANAGER = 'm'
    CUSTOMERUSER_STATUS = (
        (CUSTOMERUSER_EMPLOYEE,'employee'),
        (CUSTOMERUSER_CUSTOMER,'customer'),
        (CUSTOMERUSER_MANAGER,'manager')
    )
    birth_day = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    user_type = models.CharField(max_length=1,choices=CUSTOMERUSER_STATUS, default=CUSTOMERUSER_CUSTOMER)
    city = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='covers/', blank=True)