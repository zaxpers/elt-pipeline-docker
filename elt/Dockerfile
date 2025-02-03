FROM python:3.8-slim
RUN apt-get update && apt-get install -y cron procps
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY elt.py /app/elt.py
COPY task.py /app/task.py
COPY crontab.txt /etc/cron.d/cron-job

RUN chmod 0644 /etc/cron.d/cron-job
RUN crontab /etc/cron.d/cron-job 

CMD [ "cron","-f" ]