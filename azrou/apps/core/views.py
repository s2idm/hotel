from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from core.models import CarouselElement, Gallerie
from core.models import ImagesGallerie

class HomeView(TemplateView):
    template_name = 'home.html'
    #print(CarouselElement.objects.all().order_by('ordre'))
    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
            'carousel' :  CarouselElement.objects.all().filter(afficher=1).order_by('ordre'),
            'galleries' :  Gallerie.objects.all(),
        }
        return self.render_to_response(context)

class GallerieView(TemplateView):
    template_name = 'gallerie.html'
    #print (ImagesGallerie.objects.all())
    def get(self, request, *args, **kwargs):
        id = self.kwargs['id']

        context = {
            'some_dynamic_value': 'This text comes from django view!',
            'images': ImagesGallerie.objects.filter(gallerie__pk=id).filter(afficher=1),
        }
        return self.render_to_response(context)

