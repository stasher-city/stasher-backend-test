FROM python:3.7.2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV PYTHONPATH=/usr/src/app
ENV PYTHONUNBUFFERED=0

CMD ["gunicorn", "stasher.wsgi", "-b", "0.0.0.0:8000", "--log-file=-"]
