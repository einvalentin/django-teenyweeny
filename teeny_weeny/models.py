from django.db import models
from django.utils import timezone

class ShortLink(models.Model):
    short = models.CharField(max_length=128, unique=True)
    link = models.URLField()
    hit = models.BigIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return u'%s' % (self.short)