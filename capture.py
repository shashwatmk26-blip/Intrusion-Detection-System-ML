import pyshark

capture = pyshark.LiveCapture(interface="Wi-Fi")

capture.sniff(packet_count=10)

for packet in capture:

    try:

        print("---------------------")
        print("Protocol :", packet.highest_layer)
        print("Source :", packet.ip.src)
        print("Destination :", packet.ip.dst)

    except AttributeError:
        pass