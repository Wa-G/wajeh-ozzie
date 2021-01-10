# pull official base image
FROM ozzie6935/mangobase:latest

ENV ENVIRON=DEV

ARG city
ENV city=${city}

RUN pip install redis

COPY ./ ./

RUN groupadd -g 400 app && useradd -u 400 -g 400 app
USER app

CMD python app.py
