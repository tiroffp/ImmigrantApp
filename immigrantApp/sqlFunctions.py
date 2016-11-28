from main.models import *

# Retrieves all immmigrant records, ordered by last name
def getAllImmigrants():
	return(Immigrant.objects.order_by('immlastname'))

# Retrieves all ethnicities, in alphabetical order
def getEthnicities():
	return(Ethnicity.objects.order_by('ename'))

# Retrieves all countries, in alphabetical order
def getCountries():
	return(Country.objects.order_by('cname'))

# Retrieves all languages, in alphabetical order
def getLanguages():
	return(Languages.objects.order_by('lname'))

# Retrieves all process locations, in alphabetical order
def getProcessLocations():
	return(Processlocation.objects.order_by('plname'))

# Retrieves all continents, in alphabetical order
def getContinent():
	return(Continent.objects.order_by('cname'))

# Given names values for the many fields, will return a subset of the immigrants
def filterImmigrants(**filterParams):
	result = Immigrant.objects.all()
	if ('firstName' in filterParams):
		result = result.filter(immfirstname=filterParams['firstName'])
	if ('lastName' in filterParams):
		result = result.filter(immlastname=filterParams['lastName'])
	if ('gender' in filterParams):
		result = result.filter(immgender=filterParams['gender'])
	if ('year' in filterParams):
		result = result.filter(immdate__year=filterParams['year'])
	if ('country' in filterParams):
		#countryIDs = [country.cname for country in Country.objects.filter(cname=country)]
		#ebIDs = [eb.ebid for eb in Ethnicbackground.objects.filter(country__in=countryIDs)]
		#result = result.filter(immeb__in=ebIDs)
		result = result.filter(immeb__country=filterParams['country'])
	if ('language' in filterParams):
		#languageIDs = [lang.lname for lang in Languages.objects.filter(lname=language)]
		#ebIDs = [eb.ebid for eb in Ethnicbackground.objects.filter(spokenlang__in=languageIDs)]
		#result = result.filter(immeb__in=ebIDs)
		result = result.filter(immeb__spokenlang=filterParams['language'])
	if ('ethnicity' in filterParams):
		#ethnicIDs = [ethnicity.ename for ethnicity in Ethnicity.objects.filter(ename=ethnicity)]
		#ebIDs = [eb.ebid for eb in Ethnicbackground.objects.filter(ethnicity__in=ethnicIDs)]
		#result = result.filter(immeb__in=ebIDs)
		result = result.filter(immeb__ethnicity=filterParams['ethnicity'])
	if ('processLocation' in filterParams):
		#plocIDs = [ploc.plid for ploc in Processlocation.objects.filter(plname=processLocation)]
		#result = result.filter(immprocloc__in=plocIDs)
		result = result.filter(immprocloc__plname=filterParams['processLocation'])
	if ('destination' in filterParams):
		#cityIDs = [city.cid for city in City.objects.filter(cname=destination)]
		#result = result.filter(immdestcity__in=cityIDs)
		result = result.filter(immdestcity__cname=filterParams['destination'])
	return(result)

# Assumes all countries, ethnicity, language, process locations, cities and states exist (user chooses from a list of options)
# Creates a new immigrant record using the given values
def createImmigrant(firstName, lastName, gender, date, country, ethnicity, spokenLang, processLocation, destCity, destState):
	imm = Immigrant()
	imm.immfirstname = firstName
	imm.immlastname = lastName
	imm.immgender = gender
	imm.immdate = date
	try:
		# Attempts to find that specific ethnic background combination
		eb = Ethnicbackground.objects.get(country=country, ethnicity=ethnicity, spokenlang=spokenLang)
	except Ethnicbackground.DoesNotExist:
		# If that combination is not found, creates it
		eb = Ethnicbackground(country=country, ethnicity=ethnicity, spokenlang=spokenLang)
		eb.save()
	imm.immeb = eb
	imm.immprocloc = Processlocation.objects.get(plname=processLocation)
	try:
		# Tries to find the city (that matches the state)
		city = City.objects.get(cname=destCity, cstate=destState)
	except City.DoesNotExist:
		# If that city doesn't exist, creates it
		city = City(cname=destCity, cstate=destState)
		city.save()
	imm.immdestcity = city

	imm.save()

# Deletes an immigrant record, using its id
def deleteImmigrant(idToRemove):
	immigrant = Immigrant.objects.get(immid=idToRemove)
	immigrant.delete()