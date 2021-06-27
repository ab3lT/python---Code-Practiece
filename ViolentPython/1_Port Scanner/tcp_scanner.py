import optparse
from threading import *
import socket
from socket import *


"""
In order to better understand how our TCP port scanner works we will break our script in yo five unique steps
and write Python code for each of them. First we will input a hostname and a comma separated list of ports to scan.
Next we will translate the hostname in to an IPv4 Internet Address.
For each port in the list, we will also connect to the target address and specific port.
Finally, to determine the specific service running on the port, we will send garbage data and read the banner results
sent back by the specific application.
"""

screenLock = Semaphore(value=1)


def connScan(tgt_host, tgt_port):
    try:
        conn_skt = socket(AF_INET, SOCK_STREAM)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.send('TebelahAkram--Gudih Fela\r\n')
        results = conn_skt.recv(100)
        screenLock.acquire()
        print('[+]%d/tcp open' % tgt_port)
        print('[+] ' + str(results))
    except:
        screenLock.acquire()
        print('[+]%d/tcp closed' % tgt_port)
    finally:
        screenLock.release()
        conn_skt.close()


def portScan(tgt_host, tgt_ports):
    try:
        tgt_ip = gethostbyname(tgt_host)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % tgt_host)
        return
    try:
        tgt_name = gethostbyaddr(tgt_ip)
        print("\n [+] Scan results for: " + tgt_name[0])
    except:
        print("\n [+] Scan results for: " + tgt_ip)
    setdefaulttimeout(1)
    for tgt_port in tgt_ports:
        # print("scanning port " + tgt_port)
        t = Thread(target=connScan, args=(tgt_host, int(tgt_port)))
        t.start()
# OptionParser([usage message]) creates an instance of an option parser


def main():
    parser = optparse.OptionParser('usage % program -H' + '<target host> -p <target port>')
    parser.add_option('H', dest='tgt_host', type='string', help='specify target host')
    # parser.add_option specifies the individual command line options for our script
    parser.add_option('H', dest='tgt_port', type='int', help='specify target port')
    (options, args) = parser.parse_args()
    tgt_host = options.tgt_host
    tgt_ports = str(options.tgt_port).split(', ')
    if (tgt_host is None) | (tgt_ports[0] is None):
        print('[-] You must specify a target host and port[s].')
        exit(0)
    portScan(tgt_host, tgt_ports)


if __name__ == "__main__":
    main()


