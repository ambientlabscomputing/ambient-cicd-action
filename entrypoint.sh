#!/bin/sh

NAME=$1
DESC=$2
IMAGE=$3
REPLICAS=$4
TOKEN=$5
ORG=$6

echo "Creating service $NAME"
echo "Description: $DESC"
echo "Image: $IMAGE"
echo "Replicas: $REPLICAS"

# Create service
RESP="$(curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    -H "X-Org-Id: $ORG" \
    -d "{\"name\":\"$NAME\",\"description\":\"$DESC\",\"image\":\"$IMAGE\",\"replicas\":$REPLICAS}" \
    https://kypp7qtc6b.execute-api.us-east-1.amazonaws.com/services)"
echo "Response: $RESP"

echo "$RESP" | jq -r 'to_entries[] | "\(.key)=\(.value)"' >> "$GITHUB_OUTPUT"
