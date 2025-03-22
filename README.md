# Where_To
**Event finding web application**

"Where To" is a web application designed to simplify event discovery. 

## Present features:
- Location-based event listing; where the application lists events from closest to the user, to the farthest by utilizing the GeoDJango framework. 
- User-friendly interface; navigation is very simple, the web app being composed of only three pages: city selection page, event category selection page and event listing page.
- Administrator page (Django admin site); built through the Django library. 


## Tech stack:
- Front-end: HTML, CSS, JavaScript.
- Back-end: Python (Django).
- Database: PostgreSQL - I used the online database Neon service (https://neon.tech/)
- APIs: Google Maps API - used for coordinate retrieval from address input through the admin site.

<h3> Steps to follow: </h3>

<ol>
<li> <strong>Installing prerequisites:</strong> </li>
	
- Python 3.11 (the one I used for this project)
- Django (about version 4.2.16)
- Django rest framework (around 3.15.2)
- Django rest framework - GIS (1.0)
- psycopg2-binary (around 2.9.9)
- geopy (around 2.4.1)
- python-decouple (around 3.8)
<br>	
<li> <strong> (In Terminal) Setting up the virtual enviroment and running the server: </strong> </li>	

- After selecting the directory of the project through <code> cd </code>, you have to set up the virtual environment: <br>
<code> python manage.py migrate </code>
- Look at the code in <code>settings.py</code> and modify the indicated fields related to the database, then: <br>
<code> python manage.py migrate </code>
- Create superuser for database (add username, email, password): <br>
<code> python manage.py createsuperuser </code>
- Populate the JSON file <code>events.json</code> and then load the file to the database: <br>
<code> python manage.py loaddata </code>
- Run the server: <br>
<code> python manage.py runserver </code>
<br>
<li> <strong>Make the necessary modification:</strong></li>
- Open .env in a text editor and replace database related information (name, owner, password, host, port). Also replace <code>replace_with_your_API_key</code> with your actual API key: <br>
<code> GOOGLE_MAPS_API_KEY=replace_with_your_API_key </code> <br>
You will not have to temper with <code>settings.py</code> since the API key is filled from the .env file.
- Inside <code>static/images</code> there are two folders: <i>categories</i> and <i>cities</i> - inside these add the respective images in .png or .jpg format.

<h2><span style="color: red;">!Note: image files should have the same name as the page elements they represent, meaning that if it is called Berlin, then the image file should be <code>berlin.jpg</code></span></h2>
</ol>
<br>
<br>


	
