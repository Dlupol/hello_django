FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . .

CMD /wait && python manage.py runserver 0.0.0.0:8800