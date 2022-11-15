FROM python:3.7

WORKDIR /app

COPY ./requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./source ./source

CMD ["python", "./source/manage.py", "runserver", "0.0.0.0:8000" ]