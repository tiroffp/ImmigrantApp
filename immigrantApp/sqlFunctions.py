from models import *

def getAllImmigrants():
	return(Immigrant.objects.all())

def filterImmigrants(firstName, lastName, gender, year, country, language, ethnicity, processLocation, destination):
	result = Immigrant.objects.all()
	if (firstName != ""):
		result = result.filter(immfirstname=firstName)
	if (lastName != ""):
		result = result.filter(immlastname=lastName)
	if (gender != ""):
		result = result.filter(immgender=gender)
	if (year != ""):
		result = result.filter(immdate__year=year)
	if (country != ""):
		countryIDs = [country.cname for country in Country.objects.filter(cname=country)]
		ebIDs = [eb.ebid for eb in Ethnicbackground.objects.filter(country__in=countryIDs)]
		result = result.filter(immeb__in=ebIDs)

	return(result)