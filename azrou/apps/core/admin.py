from django.contrib import admin

# Register your models here.
from core.models import CarouselElement, ImagesGallerie, Gallerie

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('titre','sousTitre','ordre', 'afficher')
    list_editable =('sousTitre', 'ordre', 'afficher')


admin.site.register(CarouselElement, CarouselAdmin)


class ImagesGallerieAdmin(admin.ModelAdmin):
    list_display = ('gallerie', 'titre', 'image', 'ordre', 'afficher')
    list_editable =('ordre', 'afficher')


admin.site.register(ImagesGallerie, ImagesGallerieAdmin)

class GallerieAdmin(admin.ModelAdmin):
    list_display = ('titre','description')

admin.site.register(Gallerie, GallerieAdmin)




