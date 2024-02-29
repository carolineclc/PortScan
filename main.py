import socket
import sys
import ipaddress

if __name__ == '__main__':
    socket.setdefaulttimeout(0.01)
    args = sys.argv
    ip = args[1]
    init_port = 1
    end_port = 1000

    if len(args) > 2:
        try:
            init_port = int(args[2])
        except:
            sys.exit("Primeiro elemento nao e um numero valido")

    if len(args) == 4:

        try:
            end_port = int(args[3])
        except:
            sys.exit("Segundo elemento nao e um numero valido")
    try:
        ipaddress.ip_address(ip)
    except:
        sys.exit("IP nao valido")

    print('\n')
    print('**********************')
    print('[>] Escaneamento de portas no host %s' % ip)

    for ports in range(init_port, end_port + 1 ):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, ports)):
                print('[>] %s:%d/TCP Open' % (ip, ports))
                tcp.close()
        except Exception:
            pass     
    print('[>] Port Scan completo %s ' % ip)   
    print('**********************')
    