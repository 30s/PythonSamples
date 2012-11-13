from django.contrib.auth.models import User
from django.db import models

import tagging


class Widget(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User)

tagging.register(Widget)
