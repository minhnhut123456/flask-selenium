FROM --platform=linux/amd64 python:3.8

RUN apt-get update -y
RUN apt-get install -y iputils-ping

# Install Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app