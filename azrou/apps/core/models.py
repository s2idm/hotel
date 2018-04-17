from django.db import models

from django.utils.translation import ugettext_lazy as _
# Create your models here.

class CarouselElement(models.Model):
    POSITION_HELP_TEXT = _("The position of the element in the sequence or "
                           "the weight of the element in the randomization "
                           "process (depending on the carousel\'s distribution).")

    titre = models.CharField(_('Titre'), max_length=50)
    sousTitre = models.CharField(_('Sous titre'), max_length=50)
    image = models.ImageField(_('image'), upload_to='carousel_uploads')
    ordre = models.IntegerField(_('Ordre'))
    afficher = models.BooleanField(_('Afficher'))

    def __str__(self):
        return "%s" % self.titre


class Gallerie(models.Model):
    titre = models.CharField(_('Titre'), max_length=155)
    description = models.TextField(_('Description'))
    image = models.ImageField(_('image'), upload_to='carousel_uploads')

    def __str__(self):
        return "%s" % self.titre


class ImagesGallerie(models.Model):
    POSITION_HELP_TEXT = _("The position of the element in the sequence or "
                           "the weight of the element in the randomization "
                           "process (depending on the carousel\'s distribution).")
    gallerie = models.ForeignKey(Gallerie, on_delete=models.CASCADE)
    titre = models.CharField(_('Titre'), max_length=155)
    image = models.ImageField(_('image'), upload_to='carousel_uploads')

    ordre = models.IntegerField(_('Ordre'))
    afficher = models.BooleanField(_('Afficher'))

    def __str__(self):
        return "%s" % self.titre


