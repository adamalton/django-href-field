from django.db import models


class Link(models.Model):
    href = HrefField()
