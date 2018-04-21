from django.contrib import admin

# Register your models here.
from core.models import CarouselElement, ImagesGallerie, Gallerie, Contact

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('titre','sousTitre','ordre', 'afficher')
    list_editable =('sousTitre', 'ordre', 'afficher')


admin.site.register(CarouselElement, CarouselAdmin)


class ImagesGallerieAdmin(admin.ModelAdmin):
    list_display = ('gallerie', 'titre','image', 'image_thumbnail', 'ordre', 'afficher')
    list_editable =('ordre', 'afficher')


admin.site.register(ImagesGallerie, ImagesGallerieAdmin)

class GallerieAdmin(admin.ModelAdmin):
    list_display = ('titre','description','image')

admin.site.register(Gallerie, GallerieAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone','email', 'date_arriver', 'date_depart', 'adultes', 'enfants', 'message')

admin.site.register(Contact, ContactAdmin)