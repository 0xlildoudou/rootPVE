# rootPVE

## How it works
The program send a web request to the Proxmox VE api. The default Proxmox VE user is root and it's the same account of the root user of the host. By default, the realm is pam so if you find the password of the root user on Proxmox, you find the root password of the host.

The program checks the response time. If the authentication fails, the server sends a response after 3 seconds. On the other hand, if the authentication is correct, the server sends a response instantly. If the request takes more than one second to answer, the script considers the authentication as a failure.

## Usage
Run the script:
```python
python3 rootPVE.py --target <FQDN/IP> --Password <password_list>
```
### Help
```
usage: rootPVE.py [-h] --target TARGET --Password PASSWORD [--verbose] [-T T] [--timeout TIMEOUT]

options:
  -h, --help            show this help message and exit
  --target TARGET, -t TARGET
                        Proxmox VE target
  --Password PASSWORD, -P PASSWORD
                        Password file
  --verbose             Verbose mode
  -T T                  Number of Thread (default=5)
  --timeout TIMEOUT     Set timeout value (default=1)
```