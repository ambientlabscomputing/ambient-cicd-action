import json
import os
import time
from typing import List

import requests
from loguru import logger

API_URL = os.environ.get("API_URL", "https://api.ambientlabs.io")
INTERVAL = int(os.environ.get("INTERVAL", 5))


def call_run_command_api(
    token: str,
    command: str | List[str],
    timeout: int = 0,
    node_names: List[str] = [],
    node_tags: List[str] = [],
    cluster_names: List[str] = [],
    cluster_tags: List[str] = [],
    cluster_run_type: str | None = None,
    workdir: str | None = None,
    os_user: str | None = None,
    env_vars: dict | None = None,
    shell: bool = False,
) -> requests.Response:
    url = f"{API_URL}/commands/"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "command": command,
        "timeout": timeout,
        "node_options": {"node_names": node_names, "tags": node_tags},
        "store_output": True,
        "workdir": workdir,
        "os_user": os_user,
        "env_vars": env_vars,
        "shell": shell,
    }
    if cluster_names or cluster_tags:
        data["cluster_options"] = {
            "cluster_names": cluster_names,
            "tags": cluster_tags,
            "run_type": cluster_run_type,
        }
    logger.debug("Request body: {}", json.dumps(data, indent=4))
    response = requests.post(url, headers=headers, json=data)
    logger.info("response text: {}", response.text)
    response.raise_for_status()
    return response


def wait_for_command_completion(
    token, command_id: int, timeout: int = 60
) -> List[dict] | Exception:
    logger.info(f"Waiting for command completion for command_id: {command_id}")
    elapsed_time = 0
    outputs = []
    retry_count = 0
    while elapsed_time < timeout:
        logger.info(f"Elapsed Time: {elapsed_time}")
        if retry_count:
            logger.debug(f"Retry Count: {retry_count}")
        try:
            response = call_get_outputs_api(token, command_id)
        except requests.exceptions.HTTPError as e:
            logger.info(f"Error calling GET - /commands/{command_id}/outputs: {e}")
            return e
        outputs = response.json().get("results", [])
        if not outputs:
            err = "Command Input did not match to any node"
            logger.info(err)
            return Exception(err)

        # all completed is all the outputs that have status equal
        # to "failure" or "success"
        all_completed = all(
            output["status"] in ["failure", "success"] for output in outputs
        )
        if all_completed:
            return outputs

        time.sleep(INTERVAL)
        elapsed_time += INTERVAL
        retry_count += 1

    # send timeout error to stdout
    error = f"Command request timeout before receiving a response from all devices: \
{timeout} seconds elapsed.\nOutputs: {outputs}"
    print(error)
    return Exception(error)


def call_get_outputs_api(token, command_id) -> requests.Response:
    url = f"{API_URL}/commands/{command_id}/outputs"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response
