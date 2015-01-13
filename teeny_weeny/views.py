from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from .models import ShortLink
import logging

class ExpandRedirectView(RedirectView):
    logger = logging.getLogger("ExpandRedirectView")

    def get_redirect_url(self, **kwargs):
        link = get_object_or_404(ShortLink, short=kwargs.get('short_link'))
        link.hit += 1
        self.logger.debug('Expanded %s -> %s (%s hits)', link.short, link.link, link.hit)
        link.save()
        return link.link

