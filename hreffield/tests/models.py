#LIBRARIES
from django.db import models

#HREFFIELD
from hreffield.fields import HrefField


class Link(models.Model):
    href = HrefField()


class Blank(models.Model):
    blankable_href = HrefField(blank=True)
    not_blankable_href = HrefField(blank=True)


class CustomProtocols(models.Model):
    protocols = ('pigeon', 'badger', 'mailto')
    href = HrefField(protocols=protocols)


class Paths(models.Model):
    allows_paths_href = HrefField(allow_paths=True)
    no_paths_href = HrefField(allow_paths=False)


class Fragments(models.Model):
    allows_fragments_href = HrefField(allow_fragments=False)
    no_fragments_href = HrefField(allow_fragments=True)


class QueryStrings(models.Model):
    allows_query_strings_href = HrefField(allow_query_strings=True)
    no_query_strings_href = HrefField(allow_query_strings=False)
