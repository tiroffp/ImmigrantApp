from django.shortcuts import render
from immigrantApp.sqlFunctions import filterImmigrants, deleteImmigrant, createImmigrant, \
    editImmigrant, getImmigrant
from main.forms import ImmFilterForm, CreateImmForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.
def home_page(request):
    data = {
        'firstname': request.GET.get('firstname', ''),
        'lastname': request.GET.get('lastname', ''),
        'gender': request.GET.get('gender', ''),
        'country': request.GET.get('country', ''),
        'ethnicity': request.GET.get('ethnicity', ''),
        'spokenlang': request.GET.get('spokenlang', ''),
        'processLocation': request.GET.get('processLocation', ''),
    }

    form = ImmFilterForm(data)
    immigrants = filterImmigrants(firstName=data['firstname'],
                                  lastName=data['lastname'], gender=data['gender'],
                                  country=data['country'],
                                  ethnicity=data['ethnicity'], spokenLang=data['spokenlang'],
                                  procLoc=data['processLocation'])
    return render(request, 'index.html', {'immigrants': immigrants, 'form': form})


def delete_imm(request, id):

    deleteImmigrant(id)
    return HttpResponseRedirect(reverse(home_page))


def create_page(request):

    form = CreateImmForm()

    return render(request, 'create.html', {'form': form})


def edit_page(request, id):

    immigrant = getImmigrant(id)
    data = {
                    'firstname': immigrant.immfirstname,
                    'lastname': immigrant.immlastname,
                    'gender': immigrant.immgender,
                    'date': immigrant.immdate,
                    'country': immigrant.immeb.country.cname,
                    'continent': immigrant.immeb.country.ccontinent.cname,
                    'ethnicity': immigrant.immeb.ethnicity.ename,
                    'spokenlang': immigrant.immeb.spokenlang.lname,
                    'processLocation': immigrant.immprocloc.plname,
                    'city': immigrant.immdestcity.cname,
                    'state': immigrant.immdestcity.cstate.sname
                }
    form = CreateImmForm(data)
    return render(request, 'edit.html', {'form': form, 'Immigrant': immigrant})

def edit_record(request, id):
    data = {
        'firstname': request.GET.get('firstname', ''),
        'lastname': request.GET.get('lastname', ''),
        'gender': request.GET.get('gender', ''),
        'month': request.GET.get('date_month', ''),
        'day': request.GET.get('date_day', ''),
        'year': request.GET.get('date_year', ''),
        'country': request.GET.get('country', ''),
        'continent': request.GET.get('continent', ''),
        'ethnicity': request.GET.get('ethnicity', ''),
        'spokenlang': request.GET.get('spokenlang', ''),
        'processLocation': request.GET.get('processLocation', ''),
        'city': request.GET.get('city', ''),
        'state': request.GET.get('state', '')
    }

    immDate = str(data['year']) + "-" + str(data['month']) + "-" + str(data['day'])
    editImmigrant(id,firstName=data['firstname'], lastName=data['lastname'], gender=data['gender'],
                    date=immDate, country=data['country'], continent=data['continent'],
                    ethnicity=data['ethnicity'], spokenLang=data['spokenlang'],
                    processLocation=data['processLocation'], destCity=data['city'],
                    destState=data['state'])
    return HttpResponseRedirect(reverse(home_page))


def insert_record(request):

    data = {
        'firstname': request.GET.get('firstname', ''),
        'lastname': request.GET.get('lastname', ''),
        'gender': request.GET.get('gender', ''),
        'month': request.GET.get('date_month', ''),
        'day': request.GET.get('date_day', ''),
        'year': request.GET.get('date_year', ''),
        'country': request.GET.get('country', ''),
        'continent': request.GET.get('continent', ''),
        'ethnicity': request.GET.get('ethnicity', ''),
        'spokenlang': request.GET.get('spokenlang', ''),
        'processLocation': request.GET.get('processLocation', ''),
        'city': request.GET.get('city', ''),
        'state': request.GET.get('state', '')
    }

    immDate = str(data['year']) + "-" + str(data['month']) + "-" + str(data['day'])
    createImmigrant(firstName=data['firstname'], lastName=data['lastname'], gender=data['gender'],
                    date=immDate, country=data['country'], continent=data['continent'],
                    ethnicity=data['ethnicity'], spokenLang=data['spokenlang'],
                    processLocation=data['processLocation'], destCity=data['city'],
                    destState=data['state'])

    return HttpResponseRedirect(reverse(home_page))
