FROM python:3.6
MAINTAINER minhkma "nguyenvanminhkma@gmail.com"
ENV PYTHONUNBUFFERD 1
ENV SERVER_IP 192.168.100.30
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

