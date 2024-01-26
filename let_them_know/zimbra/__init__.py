"""Zimbra API."""

import sys

import requests


def get_status(zimbra_url, zimbra_name, username, password):
    """Get RFC 2445 free-busy information from calendar."""
    url = f"{zimbra_url}/home/{zimbra_name}/calendar.ifb?start=0mi&end=1mi"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        if "FREEBUSY;FBTYPE=BUSY" in response.text:
            return "busy"
        else:
            return "online"
    else:
        sys.exit(f"request to zimbra failed with {response.status_code} {response.text}")
