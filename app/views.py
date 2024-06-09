from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def alimentos(request):
    return render(request, 'app/alimentos.html')