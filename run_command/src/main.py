import os

import click
import utils
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
@click.option("--workdir", help="workdir")
@click.option("--os_user", help="os_user")
@click.option("--env_vars", help="env_vars", default=None, type=str)
@click.option(
    "--shell", help="Whether to run the command in shell", default=False, type=bool
)
def run_command(
    token: str,
    command: str,
    timeout: int = 0,
    node_names: str | None = None,
    node_tags: str | None = None,
    cluster_names: str | None = None,
    cluster_tags: str | None = None,
    cluster_run_type: str | None = None,
    workdir: str | None = None,
    os_user: str | None = None,
    env_vars: str | None = None,
    shell: bool = False,
):
    logger.debug("api_url: {}", API_URL)
    logger.info("Calling run_command API")
    if not shell:
        command = command.split(",")  # type: ignore
    if node_names:
        node_names = node_names.split(",")  # type: ignore
    if node_tags:
        node_tags = node_tags.split(",")  # type: ignore
    else:
        node_tags = []  # type: ignore
    env_dict = None
    if not cluster_names:
        cluster_names = []  # type: ignore
    else:
        cluster_names = cluster_names.split(",")  # type: ignore
    if not cluster_tags:
        cluster_tags = []  # type: ignore
    else:
        cluster_tags = cluster_tags.split(",")  # type: ignore
    if env_vars:
        logger.debug("parsing env_vars: {}", env_vars)
        env_dict = {}
        env_vars_list = env_vars.split(",")  # type: ignore
        for var in env_vars_list:
            key, value = var.split("=")
            env_dict[key] = value
        logger.debug("env_dict: {}", env_dict)
    response = utils.call_run_command_api(
        token,
        command,
        timeout,
        node_names,
        node_tags,
        cluster_names,
        cluster_tags,
        cluster_run_type,
        workdir,
        os_user,
        env_dict,
        shell,
    )
    command_data: dict = response.json()

    command_id = command_data.get("id", None)
    if command_id is None:
        logger.info(f"Error: {command_data}")
        return
    logger.info(f"Command ID: {command_id}")

    outputs = utils.wait_for_command_completion(token, command_id, timeout=int(timeout))
    logger.info(outputs)

    final_results = f"command={command},command_id={command_id},outputs={outputs}"

    print(final_results)
    if isinstance(outputs, Exception):
        raise outputs
    return


if __name__ == "__main__":
    run_command()
