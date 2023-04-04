# In-Memory Key-Value Database

## Description
This is a simple project to set, delete, dump and load data in memory. It uses a sqlite3 database to store data. Note that in the project, we have a default database with the name "default", but for security reasons, I use "default_db" instead.

## Commands
- set key value (set and store a data in database)
    - example : set city_tehran_lat 35.715298
- get key (return value of key)
    - example : get city_tehran_lat
- del key (delete record with key)
    - example : del city_tehran_lat
- keys regex (regex search in keys)
    - example : keys city_tehran.*
- use db_name (create new database)
    - example : use users_db
- list (return list of databases)
    - example : list
- dump db_name path (store a database's data in csv file in path location)
    - example : dump default_db ./dumps/default_bk
- load path db_name (restore data from csv file in path location to new database with name = db_name)
    - example : load ./dumps/default_bk default_bk
- exit (exit from program)
    - example : exit

This project is a great example of using a sqlite3 database to store data and implementing key-value pair functionalities.

### About Me
- ReZa QaVi, BS of University of Tehran
- Email: rezaqavi1379@gmail.com
- GitHub link: https://github.com/RezaQavi-git/


