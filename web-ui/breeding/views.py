from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Greetings")
    flowers = {'Cosmos': 1, 'Hyacinths': 2, 'Lilies': 3, 'Mums': 4, 'Pansies': 5, 'Roses': 6, 'Tulips': 7, 'Windflowers': 8}
    genes = {'RR': 100, 'Rr': 101, 'rr': 111, 'YY': 200, 'Yy': 201, 'yy': 211, 'WW': 300, 'Ww': 301, 'ww': 311, 'SS': 400, 'Ss': 401, 'ss': 411}
    return render(request, 'breeding/punnett.html', {'flowers': flowers, 'genes': genes})