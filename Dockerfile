FROM python:3.6.5-alpine3.7

RUN apk --no-cache add curl

COPY . .

EXPOSE 80

CMD [ "./webserver.py" ]
