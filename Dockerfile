FROM python:3.7.7-buster

EXPOSE 8000

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

COPY bin/* /opt/bin/
ENV PATH /opt/bin:$PATH
