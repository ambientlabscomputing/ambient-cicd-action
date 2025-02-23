#!/bin/sh

echo "Testing locally..."

# export GITHUB_OUTPUT
export GITHUB_OUTPUT="output.txt"
touch "$GITHUB_OUTPUT"

command="ps"
timeout=30
node_names="edgebox1"
node_tags="test"
cluster_names=""
cluster_tags=""
cluster_run_type="all"

/entrypoint.sh $TOKEN $command $timeout "${node_names}" "${node_tags}" "${cluster_names}" "${cluster_tags}" $cluster_run_type
echo "Output:"
cat "$GITHUB_OUTPUT"
