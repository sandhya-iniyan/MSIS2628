# Create bridge network. 
docker network create mynetwork

# Build db & dbadmin container and run them on the same network.
docker build -t my_db .
docker run --name mydb -itd --network mynetwork -p5432:5432 my_db

docker build -t my_dbadmin .
docker run --name mydbadmin --network mynetwork -p8080:80 -d my_dbadmin

# Build & run my_django container and mount it with the host file system
docker build -t my_django .
docker run -it --network mynetwork -p8000:8000 -v "$(pwd)/app:/app" my_django /bin/bash 
(Could meet error message like what shows in the reference. Can be solved by using quotes, which means, use "$(pwd)/app:/app" rather than $(pwd)/app:/app)

# Run under containter's /app directory
django-admin startproject web

# Run under the container's /app/web directory
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# Run this to create super user for this application
python manage.py createsuperuser
    root
    admin@admin.com
    password

# Use
http://localhost:8000

# Reference
https://stackoverflow.com/questions/48522615/docker-error-invalid-reference-format-repository-name-must-be-lowercase