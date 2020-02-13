import bisect

class Firewall:
    def __init__(self, file_name):
        self.conn_list = {}
        for conn in ["outbound", "inbound"]:
            self.conn_list[conn] = {}
            for typ in ["tcp", "udp"]:
                self.conn_list[conn][typ] = {}
                for i in range(1, 65536):
                    self.conn_list[conn][typ][i] = {}
                    self.conn_list[conn][typ][i]["start"] = []
                    self.conn_list[conn][typ][i]["end"] = [] 
        fil = open(file_name, "r")
        lines = fil.readlines()

        # Adding rules to the dictionary
        for line in lines:
            data = line.split(',')
            self.add_item(data[0], data[1], data[2], data[3])
        fil.close()

        # Sorting all ranges of IPs
        for conn in ["outbound", "inbound"]:
            for typ in ["tcp", "udp"]:
                for i in range(1, 65536):
                    if len(self.conn_list[conn][typ][i]["start"]) > 1:
                        self.conn_list[conn][typ][i]["start"], self.conn_list[conn][typ][i]["end"] = zip(*sorted(zip(self.conn_list[conn][typ][i]["start"], self.conn_list[conn][typ][i]["end"]))) 
        
    def add_item(self, conn, typ, ports, ips):
        ips_split = ips.split('-')
        ports_split = ports.split('-')
        if len(ports_split) == 1:
            ports_split.append(ports_split[0])
        ports_split[0] = int(ports_split[0])
        ports_split[1] = int(ports_split[1])
        for port in range(ports_split[0], ports_split[1]+1):
            if len(ips_split) > 1:
                self.conn_list[conn][typ][port]["start"].append(ips_split[0])
                self.conn_list[conn][typ][port]["end"].append(ips_split[1])
            else:
                self.conn_list[conn][typ][port]["start"].append(ips_split[0])
                self.conn_list[conn][typ][port]["end"].append(ips_split[0])

    def accept_packet(self, conn, typ, port, ip):
        # Finding first rule larger than said rule (binary search)
        idx = bisect.bisect_right(self.conn_list[conn][typ][port]["start"], ip)
        idx -= 1
        if idx >= 0:
            if ip <= self.conn_list[conn][typ][port]["end"][idx]:
                print("True")
                return True
        print("False")
        return False


if __name__ == "__main__":
    fw = Firewall("data")
    fil = open("test", "r")
    lines = fil.readlines()
    for line in lines:
        data = line.split(',')
        fw.accept_packet(data[0], data[1], int(data[2]), data[3])

