from django.shortcuts import render

# Create your views here.

# index function to render index template file
def index(request):
    return render(request, 'home/index.html')