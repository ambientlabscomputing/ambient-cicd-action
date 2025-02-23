FROM python:3.12-alpine

COPY run_command/entrypoint.sh /entrypoint.sh
COPY run_command/entrypoint-local.sh /entrypoint-local.sh
COPY run_command/src /src
COPY run_command/requirements.txt /requirements.txt

RUN chmod +x /entrypoint.sh
RUN chmod +x /entrypoint-local.sh

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
