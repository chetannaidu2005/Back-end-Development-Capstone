from django.contrib import admin
from .models import Concert, ConcertAttending, Photo, Song


# Register models so they appear in Django Admin
admin.site.register(Concert)
admin.site.register(ConcertAttending)
admin.site.register(Photo)
admin.site.register(Song)
