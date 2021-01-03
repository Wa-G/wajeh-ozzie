# pull official base image
FROM python:3.7.3-slim

ENV ENVIRON=DEV

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1   #### Python won’t try to write .pyc or .pyo files on the import of source modules.
ENV PYTHONUNBUFFERED 1          #### Allows log messages to be immediately dumped to the stream instead of being buffered.


RUN pip install Flask
RUN pip install mysql-connector-python

COPY ./ ./

CMD python app.py
