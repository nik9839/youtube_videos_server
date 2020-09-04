from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _

class GeneralApp(models.Model):
    title = models.CharField(_('video title'), max_length=100, blank=True)
    description = models.TextField(_('Video Description'), blank=True, null=True)
    published_at = models.DateTimeField(_('published at'), default=timezone.now)
    thumbnails = JSONField(null=True, blank=True)