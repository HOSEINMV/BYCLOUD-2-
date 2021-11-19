#HOSEIN_MV
import socket
import sys
print('''
  _         _  _               _                           _   
 | |__     | || |    __       | |      ___     _  _     __| |  
 | '_ \     \_, |   / _|      | |     / _ \   | +| |   / _` |  
 |_.__/    _|__/    \__|_    _|_|_    \___/    \_,_|   \__,_|  
_|"""""| _| """"| _|"""""| _|"""""| _|"""""| _|"""""| _|"""""| 
"`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' 

CODED BY HOSEIN_MV

OUR TELEGRAM CHANNEL:@CRACKER_CLUB AND @NH_PY AND @elf_security_cyber

SUP : @MESTER_LINUX
''')
def cloudflare():
    try:
        subdomain = ['ftp','cpanel','shop','api','mysql','secure','server','mail','webmail','direct','ip','sctp','ipv4','ipv6','ICMP','rsvp','ipsec','igmp','ecn','icmpv6','BGP','DHCP','DNS','HTTP','HTTPS','IMAP','LDAP','MGCP','MQTT','MNTP','NTP','POP','PTP','PTP','RTP','RTSP','RIP','SIP','SMTP','SNMP','SOCKS','SSH','Telnet','TLS','ssl','FTAM','ATP','DDP','NCP','ICMP','Gopher','SLIP','udp','tcp','slip','ppp','IPX','stp','nwlink','arp','dhcp','NetBEUI','CSMA','cd','SMS','NetFlow','SMB','DHCP','EIGRP','OSPF','APPLICATION','TRANSPORT','INTERNET','Interface','NEWS','BGP','DHCP','CIDR','IPX','DDP','admin','blog','host','cdn','www','YAHOO','Bluetooth','FTPS','www2','ww42','ww1','vps','vpn','ticketing','ticket','test','support','store','staging','smtp','shop','server','secure','remote','portal','pop3','pop','owa','ns','ns1','ns2','mx','mx1','m','mail1','mail2','lkjkui','img','images','image','host','hgfgdf','gw','govyty','gov','gateway','gate','forum','file','files','email','exchange'
        ,'support','help','admin','buy','1','2','1rer','2tty','documentation','app','bbs','cloud','demo','dev','docs','doc','devel','development']

        url = input("Enter Your Target with out http/https :")

        if url == "":
            try:
                print("I COULD NOT BYPASS")
                sys.exit()
            except:
                return
        for sub in subdomain:
            try:
                http = str(sub) + "." + str(url)
                bypass = socket.gethostbyname(str(http))
                print(" [!] BYPASSED BY HOSEIN MV: " + str(bypass) + ' | ' + str(http))
            except:
                pass
        try:
            input(' [*]FINISH back to menu (press enter...)')
        except:
            print("")
            sys.exit()
    except:
        print("")
cloudflare()
