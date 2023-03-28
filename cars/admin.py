from django.contrib import admin
from django.utils.html import format_html

from .models import Cars

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    # funciton inside class = deshlab self
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))
    # damit in Übersicht nicht "Thumbnail" steht sondern "Photo"
    thumbnail.short_description ='Car Image'



    list_display = ('id','thumbnail','car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured', )
    # In Suchleiste können wir nach bestimmten Sachen suchen
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
    #Filterfunktion in der Übersicht
    list_filter = ('city', 'model', 'body_style', 'fuel_type')

admin.site.register(Cars, CarAdmin)
