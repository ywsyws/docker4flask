# Docker image for Flask application
This is a repository to build a docker image for Flask application. This Docker image includes:
* Installing, setting up and configuring git account inside Docker
* Mounting volume
* Setting language code as UTF-8

## Prerequisites

It is assumed that you have
1. Already set up Docker in your local and it functions
2. Your own Flask app

Otherwise, please set up Docker and clone the whole git repository, ignoring file named **Dockerfile_w_virtual_env_TBE**


## User Manual

1. If you you have your own Flask app, copy only the Dockerfile to your work directory
2. Open Dockerfile 
    * Change Git a/c information with yours (line 13, 14)
    * **Optional:** Replace the volume directory path `/app` that needs to be mounted with yours (line 37)
    * Replace the flask app name `hello.py` to yours (line 40)
2. If you have your own Flask app, create requirements.txt file by typing `pip freeze > requirements.txt` in your work directory terminal where you flask app is
3. If you you have your own Flask app, create .gitignore file in your work directory by using [these gitignore.io templates]

**In your work directory terminal:**

4. Type `docker image build -t image_name .` to build the image
5. Use `docker images` to check if the image is successfully built
6. To create a container, type the command below and modify accordingly the `-v` tag arguments in the format of `host_path:container_path` <br>
   `docker container run -it --name container_name -p 5000:5-000 -v ~/workspace/docker:/app -d image_name`
7. Type `docker ps` to check if the container is successfuly created
8. To execute the container, type `docker exec -it container_name bash`

**Once you are inside the docker container**

9. Type `flask run --host=0.0.0.0` to run the application
10. Open the web broswer with this address: <http://127.0.0.1:5000>. If neccessary, replace `127.0.01` with your localhost IP address.

Note: If your container is stopped, you can type `docker start container_name` to restart it. Then use the command in step 8 to execute it.



[these gitignore.io templates]: https://gitignore.io/
