from __future__ import unicode_literals

from django.db import models
#import datetime

class Continent(models.Model):
    cname = models.CharField(db_column='cName', primary_key=True, max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'continent'

class Country(models.Model):
    cname = models.CharField(db_column='cName', primary_key=True, max_length=200)  # Field name made lowercase.
    ccontinent = models.ForeignKey(Continent, models.DO_NOTHING, db_column='cContinent')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'

class State(models.Model):
    sname = models.CharField(db_column='sName', primary_key=True, max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'state'

class City(models.Model):
    cid = models.AutoField(db_column='cID', primary_key=True)  # Field name made lowercase.
    cname = models.CharField(db_column='cName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cstate = models.ForeignKey('State', models.DO_NOTHING, db_column='cState', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'

class Processlocation(models.Model):
    plid = models.AutoField(db_column='plID', primary_key=True)  # Field name made lowercase.
    plname = models.CharField(db_column='plName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    plcity = models.ForeignKey(City, models.DO_NOTHING, db_column='plCity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'processlocation'

class Ethnicity(models.Model):
    ename = models.CharField(db_column='eName', primary_key=True, max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ethnicity'

class Languages(models.Model):
    lname = models.CharField(db_column='lName', primary_key=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'languages'

class Ethnicbackground(models.Model):
    ebid = models.AutoField(db_column='ebID', primary_key=True)  # Field name made lowercase.
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='country', blank=True, null=True)
    ethnicity = models.ForeignKey('Ethnicity', models.DO_NOTHING, db_column='ethnicity', blank=True, null=True)
    spokenlang = models.ForeignKey('Languages', models.DO_NOTHING, db_column='spokenLang', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ethnicbackground'

class Immigrant(models.Model):
    immid = models.AutoField(db_column='immID', primary_key=True)  # Field name made lowercase.
    immfirstname = models.CharField(db_column='immFirstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    immlastname = models.CharField(db_column='immLastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    immgender = models.CharField(db_column='immGender', max_length=45, blank=True, null=True)  # Field name made lowercase.
    immdate = models.DateField(db_column='immDate', blank=True, null=True)  # Field name made lowercase.
    immeb = models.ForeignKey(Ethnicbackground, models.DO_NOTHING, db_column='immEB', blank=True, null=True)  # Field name made lowercase.
    immprocloc = models.ForeignKey('Processlocation', models.DO_NOTHING, db_column='immProcLoc', blank=True, null=True)  # Field name made lowercase.
    immdestcity = models.ForeignKey(City, models.DO_NOTHING, db_column='immDestCity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'immigrant'