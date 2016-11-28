from django.shortcuts import render
from immigrantApp.sqlFunctions import getAllImmigrants


# Create your views here.
def home_page(request):
    immigrants = getAllImmigrants()
    print(immigrants[0].immfirstname)
    return render(request, 'index.html', {'immigrants': immigrants})