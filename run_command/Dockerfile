FROM python:3.12-alpine

COPY entrypoint.sh /entrypoint.sh
COPY entrypoint-local.sh /entrypoint-local.sh
COPY src /src
COPY requirements.txt /requirements.txt

RUN chmod +x /entrypoint.sh
RUN chmod +x /entrypoint-local.sh

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
