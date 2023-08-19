#!/bin/bash
NAME=$1
DESC=$2
IMAGE=$3
REPLICAS=$4
TOKEN=$5

echo "Creating service $NAME"
echo "Description: $DESC"
echo "Image: $IMAGE"
echo "Replicas: $REPLICAS"

# Create service
RESP="$(curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    -d "{\"name\":\"$NAME\",\"description\":\"$DESC\",\"image\":\"$IMAGE\",\"replicas\":$REPLICAS}" \
    http://localhost:8080/services)"
echo "Response: $RESP"

echo "$RESP" >> "$GITHUB_OUTPUT"
