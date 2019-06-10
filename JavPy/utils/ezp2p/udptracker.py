import socket


class UDPClient:
    def __init__(self, target_ip, target_port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.local = ("127.0.0.1", 5005)
        # self.sock.bind(self.local)
        self.server_add = (target_ip, target_port)
        self.recv = ""

    def send(self, payload):
        sent = self.sock.sendto(payload, self.server_add)
        self.recv, server = self.sock.recvfrom(4096)

    def close(self):
        self.sock.close()


if __name__ == '__main__':
    import struct
    udpc = UDPClient("62.138.0.158", 6969)
    transaction_id = 0
    data = struct.pack('!QII', 0x41727101980, 0, transaction_id)
    udpc.send(data)
    action, transaction_id, connection_id = struct.unpack("!IIQ", bytes(udpc.recv))
    peerid = b"0"
    key = 0
    data = struct.pack('!QII20s20sQQQIIIiH', connection_id, 1, transaction_id,
                       b"D02454449497A930D41D3E5ABB1537F473AA907A", peerid, 0, 0, 0, 0, 0, key, -1, udpc.local[1])

    udpc.send(data)
    print(struct.unpack("!IIB", bytes(udpc.recv)))
