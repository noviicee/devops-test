#Use base image
FROM python:3.8.0

# Copy necessary files and folders
COPY ./ ./
# path to folder to copy on *your machine* relative to build context (./)
# place to copy stuff inside *the container* (./)

#Install packages defined in the requirements.txt file
RUN pip install -r requirements.txt

# Apply all migrations
ENTRYPOINT ["./docker-entrypoint.sh"]

#Expose the application port 5000
EXPOSE 5000

# Docker Healthcheck
HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost/ || exit 1

#The application should execute at the container start
CMD ["python", "app.py"]
