FROM python:alpine

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "api/app.py", "--host=0.0.0.0"]