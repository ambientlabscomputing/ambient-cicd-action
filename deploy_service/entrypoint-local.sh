#!/bin/sh

echo "Testing locally..."

# export GITHUB_OUTPUT
export GITHUB_OUTPUT="output.txt"
touch "$GITHUB_OUTPUT"

/entrypoint.sh "test-service" "Test service" "alpine:latest" 2 "static_token" "test-org"
echo "Output:"
cat "$GITHUB_OUTPUT"
