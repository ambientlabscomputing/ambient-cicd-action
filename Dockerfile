FROM alpine:3.18.3

COPY . .

ENTRYPOINT [ "entrypoint.sh" ]
