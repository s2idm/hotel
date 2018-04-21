from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from core.models import CarouselElement, Gallerie, ImagesGallerie, Contact
import json
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie


class HomeView(TemplateView):
    template_name = 'home.html'
    #print(CarouselElement.objects.all().order_by('ordre'))
    def get(self, request, *args, **kwargs):
        context = {
            'carousel' :  CarouselElement.objects.all().filter(afficher=1).order_by('ordre'),
            'galleries' :  Gallerie.objects.all(),
            'some_dynamic_value': 'some_dynamic_value',

        }
        return self.render_to_response(context)

class GallerieView(TemplateView):
    template_name = 'gallerie.html'
    #print (ImagesGallerie.objects.all())
    def get(self, request, *args, **kwargs):
        id = self.kwargs['id']

        context = {
            'images': ImagesGallerie.objects.filter(gallerie__pk=id).filter(afficher=1),
        }
        return self.render_to_response(context)


def create_post(request):
    if request.method == 'POST':
        date_depart = request.POST.get('date_depart')
        date_arriver = request.POST.get('date_arriver')
        nom = request.POST.get('nom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        adultes = request.POST.get('adultes')
        enfants = request.POST.get('enfants')
        moyen = request.POST.get('moyen')
        response_data = {}

        post = Contact(nom=nom,date_arriver=date_arriver,date_depart=date_depart,telephone=telephone,
                       email=email,message=message,adultes=adultes,moyen=moyen,enfants=enfants)
        post.save()

        response_data['result'] = 'Create post successful!'


        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )