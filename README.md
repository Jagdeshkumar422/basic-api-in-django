run the application 
docker compose up

after run the application setup the server


after setup the server migrate the data 
python manage.py makemigrations authapp
docker compose exec web python manage.py migrate
