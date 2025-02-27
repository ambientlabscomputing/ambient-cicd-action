#!/bin/sh

echo "Testing locally..."

# export GITHUB_OUTPUT
export GITHUB_OUTPUT="output.txt"
touch "$GITHUB_OUTPUT"

command="df -h"
timeout=30
node_names="edgebox1"
node_tags="test"
cluster_names=""
cluster_tags=""
cluster_run_type="all"
workdir="/root/"
os_user="root"
env_vars='ENV1=VAL1,ENV2=VAL2'

/entrypoint.sh $TOKEN "$command" $timeout "${node_names}" "${node_tags}" "${cluster_names}" "${cluster_tags}" $cluster_run_type $workdir $os_user "$env_vars"
echo "Output:"
cat "$GITHUB_OUTPUT"
