from django.shortcuts import render
from .models import Fssbook


# Create your views here.
def index(request):
    fssbook = Fssbook.objects.all()
    return render(request, 'project_FSS/index.html', { 'cle_dic' : fssbook})

def fssbook_details(request, fssbook_slug):
    print(fssbook_slug)
    selected_fssbook= Fssbook.objects.get(slug=fssbook_slug)
    return render(request, 'project_FSS/fssbook_details.html', {
    'title_page': selected_fssbook.title,
    'description_page':selected_fssbook.desciption,
    'location_page' : selected_fssbook.localisation,
    'image_page' : selected_fssbook.image}) 
