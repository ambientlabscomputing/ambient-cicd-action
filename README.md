# Ambient Labs CI/CD Action

Allows deployment of docker applications to the Edge using Ambient Labs CI/CD services.

## Inputs

### `name`

**Required** service name.

### `description`

**Required** service description.

### `image`

**Required** docker image to deploy.

### `replicas`

**Required** number of replicas to deploy.

### `token`

**Required** Ambient Labs API token

## Outputs

### `name`

service name.

### `description`

service description.

### `image`

docker image to deploy.

### `replicas`

number of replicas to deploy.

### `compose_location`

docker compose file (not yet implemented).

### `identifier`

service Ambient identifier.

### `organization`

service organization.

### `resource_type`

service resource type.

### `status`

service status.

## Example usage

```yaml
uses: ambient-labs/ambient-labs-ci-cd-action@v1
with:
  name: 'Your Service Name'
  description: 'A brief description of your service'
  image: 'docker-image-to-deploy'
  replicas: 'number-of-replicas-to-deploy'
  token: 'your-ambient-token'
  organization: 'your-organization-id'
```

## To test locally

```bash
docker build . -t actions-test:latest
docker run -it --entrypoint /bin/sh actions-test:latest
```

Once in the container's shell, you can run the `entrypoint.sh` script to test the action locally:

```bash
/entrypoint-local.sh
```
