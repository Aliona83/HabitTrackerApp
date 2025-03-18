# Command to migrate with Docker

docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

# Docker commands

docker-compose up
docker-compose down
docker-compose build