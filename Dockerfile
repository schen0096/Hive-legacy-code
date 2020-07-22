FROM python:3.7



WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]