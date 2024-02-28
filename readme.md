# Docker demo readme

Welcome to the second part of the presentation, which will involve a bit of playing around with Docker. As a way to showcase what it can do, here is a demo project (as well as some instructions).

# Setup

As per usual, there's a bit of preparation to do. These are outlined below.

## Install Docker

These instructions differ per your operation system, but fortunately, there is [help](https://docs.docker.com/engine/install/).

## Clone this project

You probably know how to do this, but in case you don't:

```
git clone https://github.com/thomasve-DANS/docker-demo.git
```

The path doesn't matter.

# Building for the first time

When you open the project, pay close attention to the following files:

- Dockerfile; this file (by name) is the default recipe which will be executed when building your Docker container. This file is commented for your pleasure.
- docker-compose.yml; this is the file we use for local development. It's responsible for setting up the volumes, the network, and such. Again, commented for your pleasure.
- Makefile. Makefile is an older format from the C universe, which is very useful for templating commands. Don't do what you can make a machine do instead.

Once you're done reading, and have Docker installed, run:

`docker compose up --build`

You should now have a running container, as well as a local image (your first artifact).

# Usage

Feel free to head to `http://localhost:9090/docs` to see what your actions have wrought. There's a couple of endpoints to play with; they're all functions.

## Development

### Add an endpoint

Append the following code at `src/main.py`:

```
@app.get("/testpoint")
def return_example():
    return {"Here is": "An example"}

```

Note two things have just happened:

- Your container has reloaded, due to code being updated 
- Your code is now present, and when you head to `http://localhost:9090/docs`, you have an extra endpoint to use.

### Testing

Since your container has all dependencies and your code - it's sensible to do testing in there. Use the makefile for this, by running `make test` in the same directory.

### Pushing

In order to push, you need a Dockerhub account (this is free). Otherwise, it's demonstrated during the demo. The following steps are necessary:

1. Create an account at https://hub.docker.com
2. Login, go to settings > Security
3. Create a token for yourself.
4. On your own machine, run `docker login <username>` and use your token.
5. You now have cli access to your account.

Update the .env file to properly tag your image, and do:

```
docker compose build
docker compose push
```

You now have an artifact committed 

## Running

Note the second docker-compose file, which just runs the image. This is useful - we don't need to mount our code now, since everything was copied (and set up properly) during the build step.

Run it using `docker compose -f docker-compose-image.yml up` and observe that it runs with minimal instructions. It is considered good practice to not mount code on production - good artifacts work out of the box, rather than depend on a state of code.

## Detaching

Run `docker compose up -d` to run it, and detach from the image. It now runs in the background.

## Logging

Run `docker compose logs` to see logs from your container. Logging is controlled both by you (as programmer) and by the process you run.

## Monitoring usage

Run `docker stats` to observe memory footprint of your image, as well as limits. By default, images have none (but this can be set by either docker-compose or by daemon settings.)


