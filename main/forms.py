from django import forms
from immigrantApp.sqlFunctions import *

class ImmFilterForm(forms.Form):
    firstname = forms.CharField(max_length=20, required=False)
    lastname = forms.CharField(max_length=20, required=False)
    gender = forms.ChoiceField(choices=(('', 'Any'), ('Male', 'Male'), ('Female', 'Female')), required=False)

    countryChoices = tuple([('', 'Any')] + [(c.cname, c.cname) for c in getCountries()])
    country = forms.ChoiceField(choices=countryChoices, required=False)

    ethnicChoices = tuple([('', 'Any')] + [(e.ename, e.ename) for e in getEthnicities()])
    ethnicity = forms.ChoiceField(choices=ethnicChoices, required=False)

    langChoices = tuple([('', 'Any')] + [(l.lname, l.lname) for l in getLanguages()])
    spokenlang = forms.ChoiceField(choices=langChoices, required=False)

    plocChoices = tuple([('', 'Any')] + [(ploc.plname, ploc.plname) for ploc in getProcessLocations()])
    processLocation = forms.ChoiceField(choices=plocChoices, required=False)

#class ImmigrantFilrer(forms.models.modelForm)