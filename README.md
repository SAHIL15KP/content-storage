
<<<<<<< HEAD
# Content Engine with Django, Kubernetes, TailwindCSS, Twingate & More

We just released new free course (9hr+) on creating and managing a Content Engine.

But first, what is a content engine? Personally, I think sharing large projects through Google Drive is great until.... you run out of storage. I really do not want to have to "make room" for new content in 2024. 

So what to use? AWS S3. 

S3 technology is one of the best ways to store a LOT of content. But...

Navigating through AWS is a behemoth and can cause a lot of headache or errors or frustration. So what to do?

Build a simple UI that sits on top of AWS leveraging just Python, Django, a little JavaScript, and HTMX. These simple tools will allow us to manage our content in a much easier way. But....

How to share it?

First the project needs to always be running (aka deployed) so our customers/clients can access the content on their own time (e.g. Google Drive). To allow us to make it accessible all the time and primarily focusing on just our code, we use buildpacks and Kubernetes. 

While Kubernetes might sound too complex, Kubernetes is one of the best ways to deploy multiple versions of our app(s) while controlling the exact cost(s) that go into running it (in our case it's about $40/mo). Kubernetes can easily and reliably be scaled up to handle more demand (if it comes). But...

Kubernetes requires containers to run. Maybe you know how to build containers with Docker, may not  -- either way, we will use buildpacks from Google that effectively turn your GitHub repo into a PaaS, a lot like how Heroku works, to build your containers without you ever touching Docker or Dockerfiles (although Docker is awesome).

With a container in hand, Kubernetes can do its job and it does it well. But there's a catch...

We want to keep our app private. Running apps on Kubernetes are private until we make them public. So how to do we share it with others?

Enter Twingate.

Thanks to Twingate, this course exists. Also thanks to Twingate, we can securely share our private running resources with anyone we decide. Just a few simple configurations and we're off to the races. In our case, we'll configure a private Kubernetes Service (ClusterIP type) that forwards to our running containers via Kubernetes Deployments.

With this project, we leverage AWS S3's near-unlimited storage without the complicated navigation of AWS and share a work-in-progress not-yet-secure Django application to anyone we choose to build our Content Engine. Here are a few highlights of the topics we'll cover:

- Django
- Kubernetes
- Twingate
- Python Boto3 for S3 Buckets
- Uploading large files with Django, JavaScript, and Boto3
- HTMX
- TailwindCSS & Flowbite
- Auto-generate Docker Containers
- And so much more.


Each topic is covered in the exact amount of detail needed to make this course happen. The video has a number of chapters so you can skip around to the most interesting bits.

A big thank you to Twingate for partnering with me on this course! Check it out now 👇

- Watch it on Youtube: [https://youtu.be/2TX7Pal5NMc](https://youtu.be/2TX7Pal5NMc)
- Add it, for free, to your CFE library on [https://www.codingforentrepreneurs.com/courses/content-engine/](https://www.codingforentrepreneurs.com/courses/content-engine/)
=======
# Django Auto Container


This repository contains a GitHub Actions workflow that automatically builds a Django-based container application and pushes it to Docker Hub using Buildpacks.

The purpose of this repo is to help Django devs use containers without having to learn Docker. 

## Getting Started

### 1. Copy the Build Container Workflow this Repository

Navigate to your Django project directory and copy the build container workflow from this repository.

```bash
mkdir -p .github/workflows
curl https://raw.githubusercontent.com/codingforentrepreneurs/django-auto-container/main/.github/workflows/build-container.yaml > .github/workflows/build-container.yaml
```

### 2. Github Actions Secrets
In your GitHub Repo, add the following Secrets:
#### Required Secrets:
If you do not include these secrets, the container will be built but not hosted anywhere.

- `DOCKER_HUB_USERNAME`: Your Docker Hub username.
- `DOCKER_HUB_TOKEN`: Your Docker Hub access token; create a new token [here](https://hub.docker.com/settings/security).


#### Recommended Secrets:

These secrets are highly recommended to add for your specific project.
- `DOCKER_HUB_REPO`: The Docker repository to push to, in the format `username/repository`. Defaults to the format of your GitHub repo if not set -- this is where you will store your container.
- `BASE_DIR`: The default Django project location is `src/` as you see in this repo. If you have a different location, you can set it here.

#### Optional Secrets:
If you need more advanced usage, consider adding these secrets to modify how your project works.
- `BUILDPACK_BUILDER`: The buildpack builder to use. Defaults to 'heroku/buildpacks:22' if not set. Review various Heroku buildpacks [here](https://devcenter.heroku.com/articles/stack#stack-support-details)
- `DOCKER_HUB_IMAGE_TAG`: The tag to use for the Docker image. Defaults to the commit SHA (recommended) or you can set this value yourself.

### 3. Required Files

In my `BASE_DIR` (defaults to `src/`), I have the following files:
- project.toml
- requirements.txt

This files are needed to ensure the auto-container workflow runs correctly, review `src/` for working examples or use the following samples:

`project.toml`
```toml
[[build.env]]
name = "DISABLE_COLLECTSTATIC"
value = "1"

[[build.env]]
name =  "GOOGLE_RUNTIME_VERSION"
value = "3.11.7"

[[build.env]]
name = "GOOGLE_ENTRYPOINT"
value = "gunicorn cfehome.wsgi:application --bind \"0.0.0.0:$PORT\""
```
The `GOOGLE_ENTRYPOINT` is the command that will be run when the container is started. In this case, it's the production version of running `python manage.py runserver` but with `gunicorn` instead of `runserver`.


`requirements.txt`
```
Django
gunicorn
```
`gunicorn` is required as it's what is recommended to run Django in production.

### 4. Push

Push your code to GitHub and watch the magic happen. You can view the workflow in the "Actions" tab of your GitHub repo.

### 5. Run

If you have Docker installed locally, you can run your application with:

```
docker run -e PORT=8888 -p 8888:8888 <your-docker-hub-username>/<your-docker-hub-repo>:<your-docker-hub-image-tag>
```
Open [http://localhost:8888](http://localhost:8888) to view your application.

If you don't have Docker installed locally, you can run your application on any container host such as:

- Kubernetes
- Knative
- Hashicorp Nomad
- Any managed container hosting service
>>>>>>> 7aaa06d17b82687db3714004d4251da1285ce34f
