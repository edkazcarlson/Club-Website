To install a new dependancy:
1. kill images
sudo docker rmi $(sudo docker images -q)
2. while in backend/app add package with
poetry add _____
poetry install
3. Restart images with
sudo docker-compose up
or 
sudo docker-compose --verbose up

sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)

Sometimes need to remove the init() on line 17 in app/app/initial_data to do alembic upgrades