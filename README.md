# Admission_Management_System

Steps to execute the django project

1. Make sure you've installed python 3 or above.
2. Use 'pip install django' to install django package.
3. Use 'pip install pillow' to install pillow package used in database storage.
4. Open the terminal in the folder where manage.py file is located
5. Type this commands for creating database:
	python manage.py makemigrations
	python manage.py migrate
6. Finally, Run the command 'python manage.py runserver' to start the server
and open http://127.0.0.1:8000/ shown below.
7. You can now access the website.
8. Done.

Note: 
To create admin user:
In the terminal, enter the command 'python manage.py createsuperuser'