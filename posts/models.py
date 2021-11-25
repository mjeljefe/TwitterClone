from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=14, db_index=True,
    )
    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True,
    )
