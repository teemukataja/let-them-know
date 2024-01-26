"""Module configuration."""

import json

from pathlib import Path
from argparse import ArgumentParser


def load_config(path):
    """Load config file."""
    if Path(path).is_file():
        with open(path, "r") as f:
            return json.loads(f.read())


def parse_args():
    """Parse command line arguments."""
    parser = ArgumentParser()
    parser.add_argument(
        "--email",
        "-e",
        default="",
        help="your zimbra email address",
    )
    parser.add_argument(
        "--password",
        "-p",
        default="",
        help="your RC/Zimbra password, if empty, it will be prompted",
    )
    return parser.parse_args()
