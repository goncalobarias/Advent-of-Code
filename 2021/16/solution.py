from functools import reduce

with open("input.txt", "r") as file:
    packet = bin(int("1" + file.readline(), 16))[3:]

clauses = []
version_number_sum = 0
ops = {
    0: (lambda x, y: x + y),
    1: (lambda x, y: x * y),
    2: (lambda x, y: min(x, y)),
    3: (lambda x, y: max(x, y)),
    5: (lambda x, y: x > y),
    6: (lambda x, y: x < y),
    7: (lambda x, y: x == y),
}


def parse(clauses):
    global version_number_sum, packet
    len = 0
    version_number_sum += int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    packet = packet[6:]

    if type_id == 4:
        len += parse_literal(clauses)
    else:
        clauses += [[]]
        len += parse_operator(clauses[-1], type_id)

    return len + 6


def parse_literal(clauses):
    global packet
    len, literal, cont = 0, "", True

    while cont:
        if packet[0] == "0":
            cont = False
        literal += packet[1:5]
        packet = packet[5:]
        len += 5

    clauses.append([int(literal, 2)])
    return len


def parse_operator(clauses, type_id):
    global packet
    len, len_type_id, packet = 0, int(packet[0], 2), packet[1:]

    if len_type_id:
        len += parse_operator_one(clauses)
    else:
        len += parse_operator_zero(clauses)

    literal = reduce(ops[type_id], [e for clause in clauses for e in clause])
    clauses.clear()
    clauses.append(literal)
    return len + 1


def parse_operator_one(clauses):
    global packet
    len, n_sub_packets, packet = 0, int(packet[:11], 2), packet[11:]

    for _ in range(n_sub_packets):
        len += parse(clauses)

    return len + 11


def parse_operator_zero(clauses):
    global packet
    len, sub_packet_len, packet = 0, int(packet[:15], 2), packet[15:]

    while len < sub_packet_len:
        len += parse(clauses)

    return len + 15


parse(clauses)

# PART 1
print("Answer to part 1 is", version_number_sum)

# PART 2
print("Answer to part 2 is", clauses[0][0])
