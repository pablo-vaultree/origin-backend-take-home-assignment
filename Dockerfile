FROM python

COPY . .

RUN pip install -r requirements.txt

WORKDIR /api 

ENTRYPOINT ["python"]

CMD ["flask", "run", "--host=0.0.0.0"]