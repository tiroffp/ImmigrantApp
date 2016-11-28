from django.shortcuts import render
from immigrantApp.sqlFunctions import getAllImmigrants
from main.forms import ImmFilterForm


# Create your views here.
def home_page(request):
    immigrants = getAllImmigrants()
    form = ImmFilterForm()
    return render(request, 'index.html', {'immigrants': immigrants, 'form' : form})