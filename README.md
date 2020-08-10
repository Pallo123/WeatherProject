# WeatherProject
this project tells you the weather forecast of your city
To get started:
Clone the repository

Make sure pip and python are installed in the system

Type the following commands one by one in the command prompt or terminal having the project folder as the current working directory

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate 
python population_script.py 
python manage.py createsuperuser(Remember the email and password for later usage)
python manage.py runserver 
Open any web browser and type the following url: http://localhost:8000
