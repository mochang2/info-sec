# 166.104.177.24: www.hanyang.ac.kr
# HYU uses class B. /16
import socket
import time

def TCPscan():
    print("="*10 + "TCP 80/8080 scan start" + "="*10)
    
    global target # target IP
    global TCPnum # to count total number of web servers
    
    for ip_target in range(1, 255): # except network address: 0 and broadcast address: 255
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        target += str(ip_target)

        result80 = s.connect_ex((target, 80))
        result8080 = s.connect_ex((target, 8080))

        # find domain_name if exists
        target_domain_name=""
        try:
            target_domain_name = socket.gethostbyaddr(target)[0]
        except Exception as e:
            pass

        if not result80:
            TCPnum += 1
            print(target + " port 80 is open.\t" + target_domain_name)

        if not result8080:
            TCPnum += 1
            print(target + " port 8080 is open.\t" + target_domain_name)

        target = "166.104.177." 
        time.sleep(1) # not to be blocked from FW


def UDPscan(): # unreliable result
    print("="*10 + "UDP 80/8080 scan start" + "="*10)
    global target # target IP
    global UDPnum # to count total number of web servers
    
    for ip_target in range(1, 255): # except network address: 0 and broadcast address: 255
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket.setdefaulttimeout(1)

        target += str(ip_target)
        
        addr80 = (target, 80)
        addr8080 = (target, 8080)
        li = [addr80, addr8080]


        # find domain_name if exists
        target_domain_name=""
        try:
            target_domain_name = socket.gethostbyaddr(target)[0]
        except Exception as e:
            pass

            
        for i in li:
            try:
                s.sendto(b'hello', i)
                s.recvfrom(1024)
                UDPnum += 1
                print(target + " port " + str(i[1]) + " is open.\t" + target_domain_name)  # received reply
            except Exception as e:
                if str(e) == "timed out":
                    UDPnum += 1
                    print(target + " port " + str(i[1]) + " is open.\t" + target_domain_name)  # no reply
                # else: ICMP unreachable: closed
                else:
                    print("closed")

        target = "166.104.177."
        time.sleep(1) # not to be blocked from FW


#main
if __name__ == "__main__":
    start = time.time()
    target = "166.104.177." # + a
    TCPnum = 0
    UDPnum = 0

    TCPscan()
    print("\n")
    UDPscan()

    print("\n\nTotal number of web servers: TCP-" + str(TCPnum) + " UDP-" + str(UDPnum))
    print("Scan duration: " + str(round(time.time() - start)) + " sec")
