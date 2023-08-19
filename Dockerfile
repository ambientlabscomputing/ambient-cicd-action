FROM alpine:3.18.3

WORKDIR /app

COPY . .

ENTRYPOINT [ "entrypoint.sh" ]
