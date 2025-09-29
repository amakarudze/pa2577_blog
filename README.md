# pa2577_blog
A Django RESTFUL APIs blog based on two microservices, accounts and blog.

This is a blog project developed as a submission for Blekinge Institute of Technology MSc in Software Engineering 
PA2577 course Assignment 1: Build Something. The project is developed using Django and Django Rest Framework and uses 
microservice architecture.

## Prerequisites
To run this project, you need to have the following setup on your local environment:
- Docker 
- Kubernetes 
- Minikube (maybe)
- Git

## Installation
1. Clone this repository by running the command below in command line/terminal:

```git clone https://github.com/amakarudze/pa2577_blog.git```

2. Navigate into the cloned repository, by running the command below in command line/terminal:

```cd pa2577_blog```

3. In an IDE, open the file `.env_example` in either the `accounts` or `blog`folders and copy the contents into new 
files called `.env` which should be in both `accounts` and `blog` folders. The `.env` files contain environment 
environment required to run the Django apps `accounts` and `blog`.

4. Before deploying the application, first create the secrets needed for the Postgres database by running the following
command while in the root folder:

```kubectl apply -f postgres-secret.yaml```

5. To run the deployment, run the following command while still in the root folder:

```kubectl apply -f deployment.yaml```

This command create the containers for the microservices and the postgres database and runs the migration for the 
database `blog_db`, which is used by both microservices.

## Usage

To run the application, first you need to create a superuser account, to enable you to authenticate to the application. 
You can see the pod IDs by running the following command:

```kubectl get pods```

After this, you need to access one of the containers of `accounts` by running the following command:

```kubectl exec -it <<accounts_pod_id>> -- python manage.py createsuperuser```

and enter the details you want to use to create the superuser account.

After creating the superuser account, you will need to expose the APIs, at least one instance of `accounts` and 
at least one instance of `blog`. To do this, open two terminal/command line windows and navigate to the `pa2577_blog` 
folder in each of the windows.

In each of the windows, type one of the following command, with port 8000 for `accounts` API and port 8001 for `blog` API:

```kubectl port-forward <<accounts_pod_id>> 8000:8000```

```kubectl port-forward <<blog_pod_id>> 8001:8001```

Open the web browser and open the following URLs `http://127.0.0.1:8000` and `http://127.0.0.1:8001` to access the services.
Login with your user account via the `accounts` microservice and refresh the tab for the `blog` microservice and you should see
that you are also now logged into the `blog` microservice through the token acquired from the `accounts` microservice.