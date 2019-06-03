import subprocess
import json


def put(user: str, key: str, uri: str, settings: dict, group: bool = False) -> None:
    """Writes a settings payload to a CoAP URI (using the specified user and API key)."""
    payload = json.dumps(settings if group else {3311: [settings]})
    subprocess.run(
        ["coap-client", "-m", "put", "-u", user, "-k", key, "-e", payload, uri]
    )


def post(user: str, key: str, uri: str, payload: dict) -> object:
    payload_json = json.dumps(payload)
    output = subprocess.run(
        ["coap-client", "-m", "post", "-u", user, "-k", key, "-e", payload_json],
        capture_output=True,
        encoding="utf-8",
    ).stdout
    return json.loads(output.splitlines()[-1])


def get(user: str, key: str, uri: str, timeout: int = 1) -> object:
    """Reads from a CoAP URI (using the specified user and API key)."""
    process = subprocess.run(
        ["coap-client", "-m", "get", "-u", user, "-k", key, "-B", str(timeout), uri],
        capture_output=True,
        encoding="utf-8",
    )
    return json.loads(process.stdout.splitlines()[-1])
