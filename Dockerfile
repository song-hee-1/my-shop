FROM python:3.8.10

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements/local.txt

CMD ["python3", "manage.py", "runserver", "0:8000"]

EXPOSE 8000