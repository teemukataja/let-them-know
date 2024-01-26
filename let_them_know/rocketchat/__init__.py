"""Rocketchat API."""

import sys

import requests


def rc_auth(rc_url, username, password):
    """Authenticate against RocketChat API and get user id and token."""
    url = f"{rc_url}/api/v1/login"
    data = {
        "user": username,
        "password": password,
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        result = response.json()
        return result["data"]["userId"], result["data"]["authToken"]
    else:
        sys.exit(f"authentication request to rocketchat failed with {response.status_code} {response.text}")


def set_status(rc_url, user_id, token, status):
    """Set free/busy status at Rocketchat."""
    url = f"{rc_url}/api/v1/users.setStatus"
    data = {
        "status": status,
    }
    headers = {
        "X-User-Id": user_id,
        "X-Auth-Token": token,
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        pass
    else:
        sys.exit(f"set-status request to rocketchat failed with {response.status_code} {response.text}")
