# ImmigrantApp
A small Django application that allows the user to search through records of immigrants and insert, update, and delete records.

The main page of our application shows the list of immigrant records. 
  * To __filter__ this list, select values from the drop down boxes and click 'Filter'.
  * To __delete__ or __edit__ an entry from this list, select the corresponding option in the 'Actions' column.
  * To __add__ a new entry to the database, click the 'Create' button and select values for each field.


Prerequisites to run:
* Install [pip](https://pip.pypa.io/en/stable/)
 * Note: pip is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4
* Install Django and PyMySQL using pip
 * _pip install Django_
 * _pip install PyMySQL_
 * We used Django version 1.10.3 and PyMySQL version 0.7.9
 
To Run:
* Navigate to your directory and run the command _manage.py runserver_
* Find the IP address and port number for the server and type them into your internet browser
 * _http://IP Address:Port #/_
