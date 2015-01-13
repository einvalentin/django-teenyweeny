from django.contrib import admin
from .models import ShortLink

class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('short', 'link', 'hit')
    readonly_fields = ('hit', )

admin.site.register(ShortLink, ShortLinkAdmin)