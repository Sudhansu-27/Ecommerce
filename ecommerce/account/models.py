from django.db import models
# Create your models here.


from django.contrib.auth.models import AbstractUser

from ecommerce.orders.models import Order

class CustomUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")
    order = models.ForeignKey(Order , related_name='customuser' , on_delete=models.CASCADE)

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"

