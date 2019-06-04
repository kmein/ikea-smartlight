import subprocess
import json
import enum
from typing import Optional


class Method(enum.Enum):
    GET = "get"
    PUT = "put"
    POST = "post"


def run(
    method: Method,
    user: str,
    key: str,
    uri: str,
    payload: Optional[object] = None,
    timeout: Optional[int] = None,
) -> Optional[object]:
    run_process = subprocess.run(
        ["coap-client", "-m", method.value, "-u", user, "-k", key]
        + (["-e", json.dumps(payload)] if payload else [])
        + (["-B", str(timeout)] if timeout else [])
        + [uri],
        capture_output=True,
    )
    try:
        return json.loads(run_process.stdout.splitlines()[-1])
    except json.JSONDecodeError:
        return None


def put(user: str, key: str, uri: str, settings: dict, group: bool = False) -> None:
    """Writes a settings payload to a CoAP URI (using the specified user and API key)."""
    payload = settings if group else {3311: [settings]}
    run(Method.PUT, user, key, uri, payload=payload)


def post(user: str, key: str, uri: str, payload: dict) -> object:
    return run(Method.POST, user, key, uri, payload)


def get(user: str, key: str, uri: str, timeout: int = 1) -> object:
    """Reads from a CoAP URI (using the specified user and API key)."""
    return run(Method.GET, user, key, uri, timeout=timeout)
