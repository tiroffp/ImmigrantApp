from main.models import *

def getAllImmigrants():
	return(Immigrant.objects.all())

def getEthnicities():
	return([ethnicity.ename for ethnicity in Ethnicity.objects.all()])

def getCountries():
	return([country.cname for country in Country.objects.all()])

def getLanguages():
	return([lang.lname for lang in Languages.objects.all()])

def getProcessLocations():
	return([[ploc.plname, ploc.plcity.cname] for ploc in Processlocation.objects.all()])

def getContinent():
	return([cont.cname for cont in Continent.objects.all()])

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
		#countryIDs = [country.cname for country in Country.objects.filter(cname=country)]
		#ebIDs = [eb.ebid for eb in Ethnicbackground.objects.filter(country__in=countryIDs)]
		#result = result.filter(immeb__in=ebIDs)
		result = result.filter(immeb__country=country)
	if (language != ""):
		#languageIDs = [lang.lname for lang in Languages.objects.filter(lname=language)]
		#ebIDs = [eb.ebid for eb in Ethnicbackground.objects.filter(spokenlang__in=languageIDs)]
		#result = result.filter(immeb__in=ebIDs)
		result = result.filter(immeb__spokenlang=language)
	if (ethnicity != ""):
		#ethnicIDs = [ethnicity.ename for ethnicity in Ethnicity.objects.filter(ename=ethnicity)]
		#ebIDs = [eb.ebid for eb in Ethnicbackground.objects.filter(ethnicity__in=ethnicIDs)]
		#result = result.filter(immeb__in=ebIDs)
		result = result.filter(immeb__ethnicity=ethnicity)
	if (processLocation != ""):
		#plocIDs = [ploc.plid for ploc in Processlocation.objects.filter(plname=processLocation)]
		#result = result.filter(immprocloc__in=plocIDs)
		result = result.filter(immprocloc__plname=processLocation)
	if (destination != ""):
		#cityIDs = [city.cid for city in City.objects.filter(cname=destination)]
		#result = result.filter(immdestcity__in=cityIDs)
		result = result.filter(immdestcity__cname=destination)
	return(result)

# Assumes all countries, ethnicity, language, process locations, cities and states exist (user chooses from a list of options)
def createImmigrant(firstName, lastName, gender, date, country, ethnicity, spokenLang, processLocation, destCity, destState):
	imm = Immigrant()
	imm.immfirstName = firstName
	imm.immlastName = lastName
	imm.immgender = gender
	imm.immdate = date
	try:
		# Attempts to find that specific ethnic background combination
		eb = Ethnicbackground.objects.get(country=country, ethnicity=ethnicity, spokenlang=spokenLang)
	except Ethnicbackground.DoesNotExist:
		# If that combination is not found, creates it
		eb = Ethnicbackground(country=country, ethnicity=ethnicity, spokenlang=spokenLang)
		eb.save()
	imm.immeb = eb.ebid
	imm.immprocloc = Processlocation.objects.get(plname=processLocation).plid
	try:
		# Tries to find the city (that matches the state)
		city = City.objects.get(cname=destCity, cstate=destState)
	except City.DoesNotExist:
		# If that city doesn't exist, creates it
		city = City(cname=destCity, cstate=destState)
		city.save()
	imm.immdestcity = city.cid

	imm.save()