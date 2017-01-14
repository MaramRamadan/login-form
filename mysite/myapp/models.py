from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')