from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Greetings")
    flowers = {'Cosmos': 1, 'Hyacinths': 2, 'Lilies': 3, 'Mums': 4, 'Pansies': 5, 'Roses': 6, 'Tulips': 7, 'Windflowers': 8}
    return render(request, 'breeding/punnett.html', {'flowers': flowers})