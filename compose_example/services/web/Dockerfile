# pull official base image
FROM python:3.7.3-slim

ENV ENVIRON=DEV

RUN mkdir -p /usr/src/app/
ENV INSTALL_PATH /usr/src/app/
WORKDIR /usr/src/app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1   #### Python won’t try to write .pyc or .pyo files on the import of source modules.
ENV PYTHONUNBUFFERED 1          #### Allows log messages to be immediately dumped to the stream instead of being buffered.


RUN pip install --upgrade pip
COPY ./requirments.txt ./requirments.txt
RUN pip install -r ./requirments.txt


COPY ./ ./

CMD python app.py
