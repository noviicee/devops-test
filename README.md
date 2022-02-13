# Introduction

This app is written on Python and is pretty simple. 
All this App does is to count unique visitors and shows the statistic.

Running Demo of the application:

*Running Demo*
![Preview](static/screenshot.png)

*The application is currently set to eun on port:5000*.

## Requirements:

- Python `3.x` 
- PostgreSQL server
- Packages listed in `requirements.txt` 

## Installation

To install the application several steps should be completed:

- Prepare PostgreSQL database
- Install all required packages with `pip install -r requirements.txt`
- Set all required [environment variables](#configuration)
- Apply all migrations with `flask db upgrade`

## Starting the Application

- Start application

*For starting the application, I have used `python3 app.py`, but you can use different approaches - just choose one from [official docs](http://flask.pocoo.org/docs/1.0/deploying/#deployment).*

<hr>

# Application Description

So, this app has some endpoints:

- `/` - main page with all data shown
- `/version` - JSON response with current app version
- *`/healthz` - JSON response with status of the application*

## Files description

- `migrations` - directory with database migrations (see _Installation_) based on `alembic`
- `static` - just static files for serving UI
- `templates` - HTML template for main page
- `app.py` - main "executable" which contains all code
- `requirements.txt` - list of all Python packages needed to run app
- `requirements.test.txt` - list of all Python packages needed for CI/CD tasks
- `version.txt` - text file with current version

## Configuration

As any Docker-ready application - It can be easily configured via environment variables. So, here is a list of them:

- `DATABASE_URL` (required) - connection string to your database, you can find examples [here][flask-sqlalchemy-connstr].
- `USER_NAME` - your name, which will be shown on the page
- `USER_URL` - some kind of your personal URL

<hr>

# The Task

## Infrastructure

- [x] Start all related servers/instances/logical units
- [x] Make required changes in OS
- [x] Install Docker (or any other kind of containerization software)

## Containerisation

*I have made use of Docker and included a `Dockerfile`.*
*The image is built using `docker build .` and a variety of other commands. The image has also been pushed to [Dockerhub](dockerhub.com)*.

- [x] Choose right base image
- [x] Include all [installation steps](#installation)
- [x] Make this app run and listen on HTTP interface
- [x] Prepare `docker-compose.yml` for whole app stack, which can be used by developers

*Just execute  `docker-compose up` and your application would be up and running in no time.* <br>
*This is another advantage of using containerisation as we are free from the hectic task of sharing the entire code base. We can just share images and our application would be up and running on our local machine in no time.*

## Analysis 

All tools you need for this section are in `requirements.test.txt` file,
which can be easily used with `pip install -r requirements.test.txt`.

- [x] Lintering
    - [x] Code style<br/>
        I have used [flake8] to check the coding style.<br>
        ![preview](images/flake8.png) <br>
        *Here I have excluded the ./venv directory while checking for flake8 coding style because there is no need to scan it*

    - [x] Static typing<br/>
        This project can be verified with [mypy] static types checker, configuration for it can be found in `setup.cfg`

- [x] Tests<br/>
    There are no so many tests, but you can run them with `pytest .` and get successful results<br>
    ![preview](images/pytest.png)

- [x] Code coverage<br/>
    Checkout Python [Coverage] project, 
    or, you can get integration with [CodeCov] or [Coveralls] - they are free for open-source repositories.   

>*--- to be completed*

## CI/CD

Automating the project.

*I have used [Github Actions](https://docs.github.com/en/actions) for CI.*

Also,

- [ ] Database Migrations<br/>
    Application should perform DB migrations (as described above) on each deployment to update schema for new code.

- [x] Versioning<br/>
    Current project version can be seen in file `version.txt` and it will be shown as version on web-page.
    What about adding build number to this version and auto-increment it on each build?

    *I have added build number 01 to this version of the appplication and have created the [github-workflow](.github/workflows/main.yml) to trigger on each `deployment` and auto-increment the tag number on each build.*
    
## Monitoring

*I have developed the `healthz` checkpoints, which allows the users to check the status of the application.
It can be accessed on `\healthz` [endpoint](#application-description).*

## Fixes?
