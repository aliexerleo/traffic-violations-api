

FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

# 10. Build the image
# docker build -t django-app .

# 11. Run the container
# docker run -p 8000:8000 django-app

# 12. Check the container
# docker ps

# 13. Check the logs
# docker logs <container_id>

# 14. Stop the container
# docker stop <container_id>

# 15. Remove the container
# docker rm <container_id>
