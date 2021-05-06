import scapy.all as scapy
from scapy_http import http

def listen_packets(interface):
    scapy.sniff(iface=interface,store=False,prn=analiz_paketleri)
    #prn = callback function
def analiz_paketleri(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)
    
listen_packets("eth0")