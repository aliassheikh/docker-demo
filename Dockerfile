FROM thomasve/fastapi-cookiecutter-base:3.10
# In order to speed up building, we are using a base image here (built by yours truly) 
# to skip base dependency installation. This is an optimization - we now don't need to do this here.
# However, if you would like, those images are also packaged with this repo, allowing you to inspect,
# customize, or roll your own. Power to the people.

WORKDIR src
# Workdir determines the active directory inside the container we're going to use.
# Consider this a lightweight Linux VM, where you will be executing commands in specific directories

COPY src/ .
# Copy moves files from our host to the directory in question. In this case - we're copying everything
# in ./src/ to the /src directory on the host.
COPY pyproject.toml ./stub.toml
# This is a dirty little hack to present a version, but it does nicely illustrate we can copy
# both files and directories.

RUN poetry install
# Hey, what gives, we already installed dependencies, right? Correct - but in case there are extra
# dependencies, we can now strap them in, using this step. We'll show this later.

EXPOSE 9090
# Expose opens a port to be used. Basically, this allows network traffic using this port.

RUN pip install uvicorn
# In order to use uvicorn as a cli command, we need to run this little nugget.

CMD ["uvicorn", "main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "9090"]
# Finally, the command we want this container to run. This controls what this image does. Without a command,
# the image does "nothing" by default.
