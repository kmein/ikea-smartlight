import subprocess
import json


def put(user: str, key: str, uri: str, settings: dict) -> None:
    """Writes a settings payload to a CoAP URI (using the specified user and API key)."""
    payload = json.dumps({3311: [settings]})
    subprocess.run(["coap-client", "-m put", "-u", user, "-k", key, "-e", payload, uri])


def get(user: str, key: str, uri: str, timeout: int = 5) -> dict:
    """Reads from a CoAP URI (using the specified user and API key)."""
    output = subprocess.run(
        ["coap-client", "-m get", "-u", user, "-k", key, "-B", str(timeout), uri],
        capture_output=True,
    ).stdout
    return json.loads(output.splitlines()[-1])
