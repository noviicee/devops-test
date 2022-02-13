FROM python:3.8
LABEL maintainer="Anamika"

COPY ./ ./
# path to folder to copy on *your machine* relative to build context (./)
# place to copy stuff inside *the container* (./)

RUN pip install -r requirements.txt
RUN pip install -r requirements.test.txt

EXPOSE 5000

# command to run on container start
CMD [ "python3", "app.py" ]
