FROM python:slim

RUN apt-get update && apt-get install git -y --no-install-recommends


ENV APP_HOME /app
ENV PORT 8080
ENV PYTHONUNBUFFERED 1
EXPOSE $PORT
WORKDIR $APP_HOME

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT $APP_HOME/start.sh
