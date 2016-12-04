from main.models import Immigrant, Ethnicity, Country, Languages, Processlocation, Continent, \
    State, Ethnicbackground, City


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


# Retrieves all states, in alphabetical order
def getStates():
    return(State.objects.order_by('sname'))


# Given names values for the many fields, will return a subset of the immigrants
def filterImmigrants(firstName, lastName, gender, country, ethnicity, spokenLang, procLoc):
    result = Immigrant.objects.order_by('immlastname')
    if (firstName != ''):
        result = result.filter(immfirstname=firstName)
    if (lastName != ''):
        result = result.filter(immlastname=lastName)
    if (gender != ''):
        result = result.filter(immgender=gender)
    if (country != ''):
        result = result.filter(immeb__country=country)
    if (ethnicity != ''):
        result = result.filter(immeb__ethnicity=ethnicity)
    if (spokenLang != ''):
        result = result.filter(immeb__spokenlang=spokenLang)
    if (procLoc != ''):
        result = result.filter(immprocloc__plname=procLoc)

    return(result)


# Assumes all countries, ethnicity, language, process locations, cities and states exist
# (user chooses from a list of options)
# Creates a new immigrant record using the given values
def createImmigrant(firstName, lastName, gender, date, country, continent, ethnicity, spokenLang,
                    processLocation, destCity, destState):
    imm = Immigrant()
    imm.immfirstname = firstName
    imm.immlastname = lastName
    imm.immgender = gender
    imm.immdate = date

    cont = Continent.objects.get(cname=continent)

    try:
        # Attempts to find that country
        c = Country.objects.get(cname=country)
    except Country.DoesNotExist:
        # If that country is not found, creates it
        c = Country(cname=country, ccontinent=cont)
        c.save()

    try:
        # Attempts to find that ethnicity
        e = Ethnicity.objects.get(ename=ethnicity)
    except Ethnicity.DoesNotExist:
        # If that combination is not found, creates it
        e = Ethnicity(ename=ethnicity)
        e.save()

    try:
        # Attempts to find that ethnicity
        sl = Languages.objects.get(lname=spokenLang)
    except Languages.DoesNotExist:
        # If that combination is not found, creates it
        sl = Languages(lname=spokenLang)
        sl.save()

    try:
        # Attempts to find that specific ethnic background combination
        eb = Ethnicbackground.objects.get(country=country, ethnicity=ethnicity,
                                          spokenlang=spokenLang)
    except Ethnicbackground.DoesNotExist:
        # If that combination is not found, creates it
        eb = Ethnicbackground(country=c, ethnicity=e, spokenlang=sl)
        eb.save()

    imm.immeb = eb
    imm.immprocloc = Processlocation.objects.get(plname=processLocation)

    state = State.objects.get(sname=destState)

    try:
        # Tries to find the city (that matches the state)
        city = City.objects.get(cname=destCity, cstate=state)
    except City.DoesNotExist:
        # If that city doesn't exist, creates it
        city = City(cname=destCity, cstate=state)
        city.save()

    imm.immdestcity = city

    imm.save()


# Deletes an immigrant record, using its id
def deleteImmigrant(idToRemove):
    immigrant = Immigrant.objects.get(immid=idToRemove)
    immigrant.delete()


# Returns an immigrant record, using its id, for editing
def editImmigrant(id):
    return Immigrant.objects.get(immid=id)
