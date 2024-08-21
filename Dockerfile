# Command for building the container sending the build arguments.

FROM python:3.12.5

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y git

RUN mkdir task-be

WORKDIR /task-be

COPY . .

# Install python project requirements.
RUN pip install -r /task-be/requirements.txt -U

RUN chmod +x start.sh



