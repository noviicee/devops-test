# Introduction

This app is written on Python and is pretty simple. 
All this App does is to count unique visitors and shows the statistic.

Running Demo of the application: [Running Demo][demo].

![Preview](static/screenshot.png)

## Requirements:

- Python `3.x` 
- PostgreSQL server
- Packages listed in `requirements.txt` 

## Installation

To install the application several steps should be completed:

- Prepare PostgreSQL database
- Install all required packages with `pip install -r requirements.txt`
- Set all required environment variables
- Apply all migrations with `flask db upgrade`
- Start application

*For starting the application, I have used `python3 app.py`, but you can use different approaches - just choose one from [official docs][flask-deploy].*


# Application Description

So, this app has some endpoints:

- `/` - main page with all data shown
- `/version` - JSON response with current app version

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

# Task

## Infrastructure

I think the best option for this is [Terraform]. But you can also use [Ansible] or [Chef], or any tool you want. 
It will be great, if your solution can be used from the box to start whole stack on AWS.

- [x] Start all related servers/instances/logical units
- [x] Make required changes in OS
- [x] Install Docker (or any other kind of containerization software)

## Containerisation

`Dockerfile` - should be included, but it isn't, because developer of the app was too lazy for this task... 
So, it will be first step to build container with this app - writing `Dockerfile` and making first `docker build .`.

- [x] Choose right base image
- [x] Include all [installation steps](#installation)
- [x] Make this app run and listen on HTTP interface
- [x] Prepare `docker-compose.yml` for whole app stack, which can be used by developers

## Analysis 

All tools you need for this section are in `requirements.test.txt` file,
which can be easily used with `pip install -r requirements.test.txt`.

- [ ] Lintering
    - [x] Code style<br/>
        Just use [flake8] and configuration from `setup.cfg`
    - [ ] Static typing<br/>
        This project can be verified with [mypy] static types checker, configuration for it can be found in `setup.cfg`
- [x] Tests<br/>
    There are no so many tests, but you can run them with `pytest .` and get successful results
- [x] Code coverage<br/>
    Checkout Python [Coverage] project, 
    or, you can get integration with [CodeCov] or [Coveralls] - they are free for open-source repositories.   

## CI/CD

At this stage you already have project, that can be built and verified for some kind of issues. 
It's time to automate it.

Choose one of CI/CD you like:

- [ ] GitLab<br/>
    All you need - `.gitlab-ci.yml` file as described [here][gitlab-ci-yml].
- [ ] BitBucket<br/>
    You can also pass this stage using [BitBucket Pipelines][bitbucket-pipelines].
    Just implement build step and deployment somewhere - from AWS to K8s.
- [ ] Jenkins<br/>
    Most complex but more powerfull than others (IMHO). 
    If you choose it - you need to write working `Jenkinsfile` to achieve the goal.
    I recommend to use scripted, not declarative pipeline - it would be much better to show your experience.
    Documentation about Jenkins Pipelines is avaiable [here][jenkins-pipelines].

And of course don't forget about:

- [ ] Database Migrations<br/>
    Application should perform DB migrations (as described above) on each deployment to update schema for new code.
- [ ] Versioning<br/>
    Current project version can be seen in file `version.txt` and it will be shown as version on web-page.
    What about adding build number to this version and auto-increment it on each build?
    
## Monitoring

Just prepare some examples, how this app could be monitored. 
Docker Healthchecks or rules on AWS Route53 - anything will be accepted as solution.

## Documentation

Documentation should include key points such as:

- [ ] What technologies were used and what tools are needed to use your solution?
- [ ] How to start this service from scratch using your solution?

Also, you may write additional docs like:

- [ ] How to scale number of servers to take more load?
- [ ] What is application deployment architecture diagram?

To draw diagrams you can use [Draw.io][drawio], [CloudCraft] or even [ASCII Art][asciiflow]. Include them in your repository too.

## Fixes?

There are some problems in app architecture. If you have a solution - it will be great!
