from django.shortcuts import render

# Create your views here.


def leaflet_map(request):
    return render(request, 'leaflet/index.html')
