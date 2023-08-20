FROM alpine:3.18.3

COPY entrypoint.sh /entrypoint.sh
COPY entrypoint-local.sh /entrypoint-local.sh

RUN chmod +x /entrypoint.sh
RUN chmod +x /entrypoint-local.sh

# install curl
RUN apk add --no-cache curl

ENTRYPOINT ["/entrypoint.sh"]
