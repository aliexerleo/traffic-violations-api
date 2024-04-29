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

- The application can add remove update and list vehicle, person.
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

## Authors

- [@aliexerleo](https://github.com/aliexerleo/)
