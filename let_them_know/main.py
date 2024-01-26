"""Main module."""

import os
import sys
import getpass

from . import parse_args, load_config
from .zimbra import get_status
from .rocketchat import rc_auth, set_status


def main():
    """Run module."""
    # load config file from home directory
    config = load_config(os.path.expanduser("~/.let-them-know.json"))

    # get command line arguments
    args = parse_args()

    # check that name is set
    if not len(args.email) > 0:
        sys.exit("email is required")

    # create zimbra username
    zimbra_name = args.email.split("@")[0]

    # get username and password for API auth
    username = getpass.getuser()
    password = args.password
    if password == "":
        password = getpass.getpass("Email/Rocketchat password: ")

    # get free-busy status from zimbra calendar
    zimbra_status = get_status(config["zimbra"].rstrip("/"), zimbra_name, username, password)

    # authenticate user at rocketchat API
    user_id, token = rc_auth(config["rocketchat"].rstrip("/"), username, password)

    # set free-busy status in rocketchat
    set_status(config["rocketchat"].rstrip("/"), user_id, token, zimbra_status)

    # confirmation
    print(f"rocketchat status set to {zimbra_status}")


if __name__ == "__main__":
    main()
