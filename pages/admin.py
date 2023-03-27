from django.contrib import admin
from .models import Teams
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    # funciton inside class = deshlab self
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))
    # damit in Übersicht nicht "Thumbnail" steht sondern "Photo"
    thumbnail.short_description ='Photo'

    # was angezeigt wird auf Übersicht
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date')
    # was anklickbar sein soll
    list_display_links = ('id', 'thumbnail', 'first_name',)
    # Suchfeld oben - nach welchem Kriterien kann gesucht werden
    search_fields = ('first_name', 'last_name', 'designation')
    # FIlterfunktion - auf der rechten Seite
    list_filter = ('designation',)

# Register your models here.
admin.site.register(Teams,TeamAdmin)