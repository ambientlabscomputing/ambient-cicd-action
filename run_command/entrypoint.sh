#!/bin/sh

# token
# command
# timeout
# node_names
# node_tags
# cluster_names
# cluster_tags
# cluster_run_type

TOKEN=$1
COMMAND=$2
TIMEOUT=$3
NODE_NAMES=$4
NODE_TAGS=$5
CLUSTER_NAMES=$6
CLUSTER_TAGS=$7
CLUSTER_RUN_TYPE=$8
WORKDIR=$9
OS_USER=${10}
ENV_VARS=${11}

echo "Running command: $COMMAND"
echo "Timeout: $TIMEOUT"

echo "START TIME: $(date)"

command="python /src/main.py \
    --token $TOKEN \
    --command '$COMMAND' \
    --timeout $TIMEOUT \
    --node_names $NODE_NAMES \
    --node_tags $NODE_TAGS \
    --cluster_names $CLUSTER_NAMES \
    --cluster_tags $CLUSTER_TAGS \
    --cluster_run_type $CLUSTER_RUN_TYPE \
    --workdir $WORKDIR \
    --os_user $OS_USER \
    --env_vars "$ENV_VARS"
"

echo "Running command: $command"

# Wait for the command to finish
FinalResults="$(eval $command)"

echo "END TIME: $(date)"

# Write the results to the output file
echo "$FinalResults" >> "$GITHUB_OUTPUT"
