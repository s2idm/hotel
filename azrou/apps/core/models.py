from django.db import models

from django.utils.translation import ugettext_lazy as _
# Create your models here.

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

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
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(400, 300)],
                                      format='JPEG',
                                      options={'quality': 60})
    ordre = models.IntegerField(_('Ordre'))
    afficher = models.BooleanField(_('Afficher'))

    def __str__(self):
        return "%s" % self.titre



class Contact(models.Model):
    POSITION_HELP_TEXT = _("The position of the element in the sequence or "
                           "the weight of the element in the randomization "
                           "process (depending on the carousel\'s distribution).")

    nom = models.CharField(_('Titre'), max_length=50)
    telephone = models.CharField(_('Telephone'), max_length=50)
    email = models.CharField(_('Email'), max_length=50)
    date_arriver = models.CharField(_("Date d'arriver"), max_length=50)
    date_depart = models.CharField(_("Date de départ"), max_length=50)
    message = models.TextField(_('Message'), max_length=300)
    adultes = models.CharField(_('Adultes'), max_length=50)
    enfants = models.CharField(_('Enfants'), max_length=50)
    moyen = models.CharField(_('moyen de contact preféré'), max_length=50)



    def __str__(self):
        return "%d" % self.pk