from django import forms
from immigrantApp.sqlFunctions import *
from django.forms.extras import SelectDateWidget

class ImmFilterForm(forms.Form):
    firstname = forms.CharField(max_length=20, required=False, label="First Name")
    lastname = forms.CharField(max_length=20, required=False, label="Last Name")
    gender = forms.ChoiceField(choices=(('', 'Any'), ('Male', 'Male'), ('Female', 'Female')), required=False, label="Gender")

    countryChoices = tuple([('', 'Any')] + [(c.cname, c.cname) for c in getCountries()])
    country = forms.ChoiceField(choices=countryChoices, required=False, label="Home Country")

    ethnicChoices = tuple([('', 'Any')] + [(e.ename, e.ename) for e in getEthnicities()])
    ethnicity = forms.ChoiceField(choices=ethnicChoices, required=False, label="Ethnicity")

    langChoices = tuple([('', 'Any')] + [(l.lname, l.lname) for l in getLanguages()])
    spokenlang = forms.ChoiceField(choices=langChoices, required=False, label="Language")

    plocChoices = tuple([('', 'Any')] + [(ploc.plname, ploc.plname) for ploc in getProcessLocations()])
    processLocation = forms.ChoiceField(choices=plocChoices, required=False, label="Process Location")


class CreateImmForm(forms.Form):
    firstname = forms.CharField(max_length=20, label="First Name")
    lastname = forms.CharField(max_length=20, label="Last Name")
    gender = forms.ChoiceField(choices=(('Male', 'Male'), ('Female', 'Female')),label="Gender")
    date = forms.DateField(widget = SelectDateWidget(years=range(1900,1960)), label="Immigration Date")
    country = forms.CharField(max_length=20, label="Home Country")

    continentChoices = tuple([(c.cname, c.cname) for c in getContinent()])
    continent = forms.ChoiceField(choices=continentChoices, label="Continent")

    ethnicity = forms.CharField(max_length=20, label="Ethnicity")
    spokenlang = forms.CharField(max_length=20, label="Language")

    plocChoices = tuple([(ploc.plname, ploc.plname) for ploc in getProcessLocations()])
    processLocation = forms.ChoiceField(choices=plocChoices, label="Process Location")

    city = forms.CharField(max_length=20, label="Destination City")

    stateChoices = tuple([(s.sname, s.sname) for s in getStates()])
    state = forms.ChoiceField(choices=stateChoices, label="Destination State")
