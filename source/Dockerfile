FROM python:3.6

WORKDIR /usr/app

ADD ./requirements ./
RUN pip install -r requirements.txt
ADD ./app.py ./

CMD ["python", "app.py"]
