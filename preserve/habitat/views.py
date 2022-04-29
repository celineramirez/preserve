from django.shortcuts import render
from .models import Habitat
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    habitats = Habitat.objects.all()

    return render(request, 'habitat/post_list.html', {'habitats': habitats})

def post_detail(request, pk):
    habitat = get_object_or_404(Habitat, pk=pk)
    return render(request, 'habitat/post_detail.html', {'habitat': habitat})