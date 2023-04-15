# Sound Oasis - Music Streaming Website
Sound Oasis is a Django-based music streaming website that allows users to discover and listen to their favorite music. The website is deployed on Amazon AWS and can be accessed via the domain "sound-oasis.studio"<hr><hr>

 ## Features<hr>
- Playlists: Users can create, edit, and manage their own playlists. They can also add songs from the music catalog to their playlists.
- Audio streaming: Users can listen to songs directly on the website using the built-in audio player. The player supports play, pause, next, and previous functionality.
- Responsive design: The website is designed to be mobile-friendly and responsive, allowing users to access it on various devices, including desktops, tablets, and smartphones.

## Technologies Used<hr>
- Django: A high-level Python web framework for building web applications.
- Amazon AWS: The website is deployed on AWS using services such as EC2 for virtual server hosting.
- Tailwind CSS: A popular CSS framework for building modern and responsive user interfaces.
- SQLite: A self-contained, serverless, and zero-configuration relational database management system used as the backend database for the website.
- HTML5, CSS3, and JavaScript: The standard web technologies used for building the frontend user interface and interactivity.

## Deployment
The website is deployed on Amazon AWS and can be accessed via the domain "sound-oasis.studio". To deploy the website locally or on your own server, follow these steps:

1. Clone the repository,
```bash
git clone https://github.com/nirakar24/Music_streaming_website.git
```
2. Create and activate a virtual environment: 
```python
python -m venv venv 
```
``` python
source venv/bin/activate #(for Unix-based systems) 
```
```python
venv\Scripts\activate #(for Windows).
```
3. Install the dependencies:
``` python
pip install -r requirements.txt
```
4.Set up the database: 
```python
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser for admin access: 
```pyhton
python manage.py createsuperuser
```
6. Start the development server: 
```python
python manage.py runserver
```
7. Access the website in your web browser at http://localhost:8000/

### Note: Make sure to set up your own AWS credentials and update the settings file with the correct configurations for AWS services.

## Contributing
Contributions to Sound Oasis are welcome! If you'd like to contribute to the project, please follow the steps below:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: 
```bash
git checkout -b feature-branch
```
3. Make your changes and test thoroughly.
4. Commit your changes: 
```bash
git commit -m "Description of changes"
```
5. Push your changes to your forked repository:
```bash
 git push origin feature-branch
 ```
6. Create a pull request to the main repository with your changes.
7. Please ensure that your code follows the coding style and guidelines of the project and includes appropriate documentation.

## License

Sound Oasis is released under the [MIT](https://choosealicense.com/licenses/mit/) License, which is an open-source license that allows you to use, modify, and distribute the code for personal and commercial purposes. However, it comes with no warranty or support. Please see the license file for more details.


