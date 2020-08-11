############################################################
# Dockerfile to build Python / Django / Mysql small container images
# Based on Linux Alpine
############################################################

FROM python:3.8.2-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
	&& apk add --virtual build-deps gcc python3-dev musl-dev \
	&& apk add --no-cache mariadb-connector-c-dev
RUN pip install mysql

RUN pip install --upgrade pip && pip install --no-cache-dir \
	asgiref==3.2.3 \
	Django==3.0.3 \
	django-cors-headers==3.2.1 \
	djangorestframework==3.11.0 \
	mysqlclient==1.4.6 \
	python-dotenv==0.10.5 \
	pytz==2019.3 \
	sqlparse==0.3.0 \
	requests==2.23.0 \
	django-url-filter==0.3.15 \
	django-filter==1.1.0

# Limpa espaço em disco
RUN apk del build-deps musl-dev gcc python3-dev
RUN rm -Rf ~/.cache

COPY . /app

WORKDIR /app

EXPOSE 8000

CMD ["sh", "./start_django.sh"]
