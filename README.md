# Blog

How to install

clone project : 

* git clone https://github.com/erfederuiz/kcpractice_20170625_django.git

After you have done with clone the repo.


Now you have to create a virtual environment and activate it:

* virtualenv .
* chmod -R 777 .
* bin/activate

In your virtual environment you need to  install all the dependencies.


Go to the project directory `project`


* pip3 install --upgrade -r requirements.txt


After Done with Installation, start your project:

* python3 manage.py runserver


You can create an admin user

* python3 manage.py createsuperuser

You can empty previous data in the database

* python3 manage.py flush
