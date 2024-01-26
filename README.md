# Let Them Know
`ltk` is a script which checks your Zimbra calendar status for the next minute, and updates your RocketChat status to `busy` if you have a meeting, and to `online` if you have no meetings.

## Configuration
Add your Zimbra and RocketChat addresses to [.let-them-know.json](.let-them-know.json) and place the file to your home directory.

## Usage

### Installation
To install pip module and use the `ltk` command
```
pip install .
ltk --help
```

To run as a module with python (without installing)
```
pip install -r requirements.txt
python -m let_them_know.main --help
```

### Examples
Prompt password
```
ltk --email 'me@domain.org'
Email/Rocketchat password:
rocketchat status set to online
```

Supply password (read it from an env, so it doesn't get saved to shell)
```
ltk --email 'me@domain.org' --password $PASSWORD
rocketchat status set to online
```

Crontab for running the script once a minute for each workday (mon-fri, 8-16)
```
* 8-16 * * 1-5 ltk --email 'me@domain.org' --password $PASSWORD
```
