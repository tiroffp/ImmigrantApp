from django.shortcuts import render
from immigrantApp.sqlFunctions import getAllImmigrants
from main.forms import ImmFilterForm


# Create your views here.
def home_page(request):
    data = {
        'firstname':request.GET.get('firstname',''),
        'lastname':request.GET.get('lastname',''),
        'gender':request.GET.get('gender',''),
        'country':request.GET.get('country',''),
        'ethnicity':request.GET.get('ethnicity',''),
        'spokenlang':request.GET.get('spokenlang',''),
        'processLocation':request.GET.get('processLocation',''),
    }

    form = ImmFilterForm(data)
    immigrants = getAllImmigrants()
    return render(request, 'index.html', {'immigrants': immigrants, 'form' : form})