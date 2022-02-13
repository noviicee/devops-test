FROM python:3.8
LABEL maintainer="Anamika"

COPY ./ ./
# path to folder to copy on *your machine* relative to build context (./)
# place to copy stuff inside *the container* (./)

RUN pip install -r requirements.txt

HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost/ || exit 1

# Docker Healthcheck

EXPOSE 5000

# command to run on container start
CMD [ "python3", "app.py" ]
