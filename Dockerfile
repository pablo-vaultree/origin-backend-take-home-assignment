FROM python

COPY . .

RUN pip install -r requirements.txt

WORKDIR /api 

ENTRYPOINT ["python"]

CMD ["app.py", "--host=0.0.0.0"]