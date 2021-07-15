from django.db import models
from Src.Domain.Entities.User import User
import datetime


class Carts(models.Model):
    cart_id = models.BigAutoField(primary_key=True, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.IntegerField()
    creation_date = models.DateTimeField(default=datetime.datetime.now)

