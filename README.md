# Docker image for Flask application
This is a repository to build a docker image for Flask application. This Docker image includes:
* Installing, setting up and configuring git account inside Docker
* Mounting volume
* Setting language code as UTF-8
<br>

## Prerequisites

It is assumed that you have
1. Already set up Docker in your local and it functions
2. Your own Flask app

Otherwise, please set up Docker and clone the whole git repository, ignoring file named **Dockerfile_w_virtual_env_TBE**

<br>

## User Manual

1. If you you have your own Flask app, copy only the Dockerfile to your work directory
2. Open Dockerfile 
    * Change Git a/c information with yours (line 13, 14)
    * **Optional:** Replace the volume directory path `/app` that needs to be mounted with yours (line 37)
    * Replace the flask app name `hello.py` to yours (line 40)
3. If you have your own Flask app, create requirements.txt file by typing `pip freeze > requirements.txt` in your work directory terminal where you flask app is
4. If you have your own Flask app, go to [gitignore.io] to create .gitignore file in your work directory
<br>

### In your work directory terminal:

5. Type `docker image build -t image_name .` to build the image
6. Use `docker images` to check if the image is successfully built
7. To create a container, type the command below and modify accordingly the `-v` tag arguments in the format of `host_path:container_path` <br>
   `docker container run -it --name container_name -p 5000:5-000 -v ~/workspace/docker:/app -d image_name`
<br>

### Open your broswer

8. Go to this address: <http://127.0.0.1:5000> to see the page. If neccessary, replace `127.0.01` with your localhost IP address. 
<br>
<br>

#### If your container is stopped

1. Type `docker start container_name` to restart it
2. To execute the container, type `docker exec -it container_name bash`

#### Once you are inside the docker container

3. Type `flask run --host=0.0.0.0` to run the application

Note: You can type `docker ps` in your work dorectory terminal to check if the container is successfuly created

[gitignore.io]: https://gitignore.io/
