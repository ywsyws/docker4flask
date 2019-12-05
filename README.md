# Docker image for Flask application
This is a repository to build a docker image for Flask application. This Docker image includes:
* Install, setup and configure git account
* Mount volume
* Setting language code as UTF-8

## User Manual

1. Copy the Dockerfile to your work directory.
2. Change 
    * Git a/c information (line 13, 14)
    * Volume directory needs to be mounted (line 37)
    * File name of the flask app (line 40)
2. Create requirements.txt file by typing `pip freeze > requirements.txt` in your work directory terminal, where you flask app is
3. Create .gitignore file in your work directory by using [these gitignore.io templates] 
4. In your work directory terminal, type `docker image build -t image_name .` to build the image
5. Use `docker images` to check if the image is successfully built
6. To create a container, type `docker container run -it --name container_name -p 5000:5-000 -d image_name`
7. Type `docker ps` to check if the container is successfuly built
8. To execute the container, type `docker exec -it container_name bash`
9. Once you are inside the docker container, type `flask run --host=0.0.0.0` to run the application
10. Open the web broswer with this address: <http://127.0.0.1:5000>

Note: If your container is stopped, you can type `docker start container_name` to restart it. Then use the command in step 8 to execute it.



[these gitignore.io templates]: https://gitignore.io/
