To install a new dependancy:
1. kill images
sudo docker rmi $(sudo docker images -q)
or 
sudo docker rmi $(sudo docker images -a)
2. while in backend/app add package with
poetry add _____
poetry install
3. Restart images with
sudo docker-compose up
or 
sudo docker-compose --verbose up

sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)