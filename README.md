# traffic-violations-api
A simple API to management traffic violations. It based in Django and Django rest framework

## Installation
Step by step to running the app

```bash
   git clone https://github.com/aliexerleo/traffic-violations-api.git
   cd traffic-violations-api/
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cd traffic_violations
   python manage.py runserver
   python manage.py makemigrations
   python manage.py migrate
```
For checking the app go to the http://127.0.0.1:8000/

## Features

- The application can add remove update and list vehicle and person.
- For management officials the application use the User native model of django. For add new officila/user you must be the django admin dashboard. And only the application can delete and edit name of officials.
- For load new infraction you must follow this step.
    use postman.
    Make a request POST to generate token. In this request you need send user and password of any official.
    # example request 
    type: 
    POST
    URL:
    localhost:8000/login
    ```bash
    body
        {
        "username":"David",
        "password": "Brasil2014"
        }
    ```
    After that you can make a request to load new infraction with the token and infraction data in the body.
    # example request
    type: 
    POST
    URL:
    localhost:8000/load 
     ```bash
     body
        {
        "licence": "HGO315",
        "date_incidence": "",
        "official_comment": "Traffic accident",
        "email": "sami@gmail.com"
        }
    ```
- Checking traffic violations of specific person
    # example request 
    type: 
    GET
    URL:
    localhost:8000/report
    ```bash
    body
       {
        "email": "sami@gmail.com"
       }
    ```

## Docker instructions

You need download the docker image from docker-hub. And Run the container
```bash
   docker login
   docker pull aliexerleo/crud-django-traffic-app-docker
   docker run -p 8000:8000 aliexerleo/crud-django-traffic-app-docker
```
For checking the app go to the http://127.0.0.1:8000/

## Architecture

                ┌───────────────────────────────────────────────┐
                │                   AWS Cloud                    │
                │                                               │
                │      ┌──────────────────────────────┐         │
                │      │            VPC               │         │
                │      └─────────────┬────────────────┘         │
                │                    │                           │
                │                    │                           │
                │                    ▼                           │
                │      ┌──────────────────────────────┐         │
                │      │         EC2 Instance         │         │
                │      └─────────────┬────────────────┘         │
                │                    │                           │
                │                    │                           │
                │                    ▼                           │
                │      ┌──────────────────────────────┐         │
                │      │       PostgreSQL DB         │         │
                │      └──────────────────────────────┘         │
                └───────────────────────────────────────────────┘


## Explanation:

- AWS Cloud: Represents the cloud environment provided by Amazon Web Services.
- VPC (Virtual Private Cloud): A virtual network dedicated to your AWS account. It enables you to launch AWS resources into a virtual network that you've defined.
- EC2 Instance: An Amazon Elastic Compute Cloud (EC2) instance, which represents a virtual server in the cloud. In this setup, the EC2 instance could be running your application or web server.
- PostgreSQL DB: Represents a PostgreSQL database instance running in the AWS cloud. It could be hosted on an RDS (Relational Database Service) instance or on an EC2 instance itself.

This diagram provides a high-level overview of how these components might be set up in the AWS cloud. Depending on your specific requirements, there could be additional components, such as security groups, subnets, route tables, and so on, that need to be configured within the VPC to ensure proper network isolation and security.

## Authors

- [@aliexerleo](https://github.com/aliexerleo/)
