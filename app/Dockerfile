FROM python:3.8

EXPOSE 5000

WORKDIR /app

COPY . /app
RUN pip install  -r requirements.txt --upgrade pip

CMD python app.py