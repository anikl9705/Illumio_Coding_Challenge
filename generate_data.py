import random

conn_types = ["inbound", "outbound"]
typs = ["tcp", "udp"]

fil = open("data", "w")

for i in range(0, 10000):
    conn = conn_types[random.randint(0, 1)]
    typ = typs[random.randint(0, 1)]
    start = random.randint(1, 65535)
    ports = str(start)
    if random.random() > 0.7:
        ports += "-"
        ports += str(random.randint(start, 65535))
    ip_start = [random.randint(0, 255) for j in range(4)]
    ips = str(ip_start[0]) + "." + str(ip_start[1]) + "." + str(ip_start[2]) + "." + str(ip_start[3])
    if random.random() > 0.7:
        diff_idx = random.randint(0, 3)
        ip_end = [ip_start[j] for j in range(4)]
        ip_end[diff_idx] = random.randint(ip_start[diff_idx], 255)
        for j in range(diff_idx+1, 4):
            ip_end[j] = random.randint(0, 255)
        ips += "-" + str(ip_end[0]) + "." + str(ip_end[1]) + "." + str(ip_end[2]) + "." + str(ip_end[3])
    fil.write(conn + "," + typ + "," + ports + "," + ips + "\n")

    

