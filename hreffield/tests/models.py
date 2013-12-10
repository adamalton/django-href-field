#LIBRARIES
from django.db import models

#HREFFIELD
from hreffield.fields import HrefField


class Link(models.Model):
    href = HrefField()


class Blank(models.Model):
    href = HrefField(blank=True)


class CustomProtocols(models.Model):
    protocols = ('pigeon', 'badger', 'mailto')
    href = HrefField(protocols=protocols)


class NoFragments(models.Model):
    href = HrefField(allow_fragments=False)


class NoQueryStrings(models.Model):
    href = HrefField(allow_query_strings=False)
