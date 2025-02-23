import click
import os
import sys
import utils
from typing import List
from loguru import logger

API_URL = os.environ.get("API_URL", "https://api.ambientlabs.io")

# token
# command
# timeout
# node_names
# node_tags
# cluster_names
# cluster_tags
# cluster_run_type
@click.command()
@click.option("--token", help="token")
@click.option("--command", help="command")
@click.option("--timeout", help="timeout")
@click.option("--node_names", help="node_names")
@click.option("--node_tags", help="node_tags")
@click.option("--cluster_names", help="cluster_names")
@click.option("--cluster_tags", help="cluster_tags")
@click.option("--cluster_run_type", help="cluster_run_type")
def run_command(token: str, command: str, timeout: int = 0, node_names: List[str] = [], node_tags:  List[str] = [], cluster_names:  List[str] = [], cluster_tags:  List[str] = [], cluster_run_type: str | None = None):
    logger.debug(f"run_command() - API_URL: {API_URL}")
    logger.info("Calling run_command API")
    response = utils.call_run_command_api(
        token, command, timeout, node_names, node_tags, cluster_names, cluster_tags, cluster_run_type
    )
    command_data: dict = response.json()

    command_id = command_data.get("id", None)
    if command_id is None:
        logger.info(f"Error: {command_data}")
        return
    logger.info(f"Command ID: {command_id}")

    outputs = utils.wait_for_command_completion(token, command_id, timeout=int(timeout))
    logger.info(outputs)

    # send outputs to stdout
    if isinstance(outputs, Exception):
        print(outputs)
        raise outputs
    for output in outputs:
        print(f"Node: {output['node_id']}\nStatus: {output['status']}\n===Output===\n{output['output']}\n===End Output===\n")
    return


if __name__ == "__main__":
    run_command()
