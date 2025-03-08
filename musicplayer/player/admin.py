
from .models import Playlist
from django.contrib import admin
from .models import Song

admin.site.register(Song)


admin.site.register(Playlist)