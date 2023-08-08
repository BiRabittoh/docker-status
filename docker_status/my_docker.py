import json
import docker, requests

with open("config.json", "r") as in_file:
    services = json.loads("".join(in_file.readlines()))
services = sorted_dict = dict(sorted(services.items()))

docker_client = docker.from_env()

def healthcheck(container, status):
    container_name = container["name"]
    try:
        container_status = status[container_name]
        if container_status != "running" or container["test"] is None:
            return status[container_name]
    except KeyError:
        return "missing"
    
    try:
        result = requests.get(container["test"]).status_code
        if result == 200:
            return "healthy"
        print(f"Status Code for {container_name} is {result}.")
    except Exception as e:
        print(e)
    return "unhealthy"

def update_status():
    containers = docker_client.containers.list(all=True)
    status = { container.name: container.status for container in containers }
    
    for k, v in services.items():
        service_status = []
        for container in v["containers"]:
            container_name = container["name"]
            container["status"] = healthcheck(container, status)
    return services

if __name__ == "__main__":
    print(update_status())
    print(services)
