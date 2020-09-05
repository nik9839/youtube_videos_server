from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _

# Model for storing videos list
class Videos(models.Model):
    title = models.CharField(_('video title'), max_length=1000, blank=True)
    description = models.TextField(_('Video Description'), blank=True, null=True)
    published_at = models.DateTimeField(_('published at'), default=timezone.now, db_index=True)
    thumbnails = JSONField(null=True, blank=True)


# Model for storing youtube api keys
class YoutubeKeys(models.Model):
    key = models.CharField(_("api key"), max_length=50)
    added_at = models.DateTimeField(_('created at'), auto_now_add=True)
    quote_reached = models.BooleanField(_("api quota reached"), default=False)