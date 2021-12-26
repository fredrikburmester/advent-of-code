"""
"""
import time
from utils.helpers import *


def part1(input_list):
    """ Part 1 and 2 """
    hex_dict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    version_sum = 0
    packet = "".join([hex_dict[x] for x in input_list[0]])

    def get_from_binary(packet):
        res = int(packet[:3], 2)
        return res, packet[3:]

    def get_length(packet, n):
        return int(packet[:n], 2), packet[n:]

    def process_packet(packet):
        nonlocal version_sum
        version, packet = get_from_binary(packet)
        version_sum += version

        t_id, packet = get_from_binary(packet)
        if t_id == 4:
            group = ""
            while True:
                group += packet[1:5]
                c = packet[0]
                packet = packet[5:]
                if c == '0':
                    break
            return packet, int(group, 2)
        else:
            len_t_id = packet[0]
            packet = packet[1:]
            subpacket_versions = []
            subpacket_versions = []
            if len_t_id == '0':
                subpackets_length, packet = get_length(packet, 15)
                subpackets = packet[:subpackets_length]
                while subpackets:
                    subpackets, version = process_packet(subpackets)
                    subpacket_versions.append(version)
                packet = packet[subpackets_length:]
            else:
                nr_of_subpackets, packet = get_length(packet, 11)
                for _ in range(nr_of_subpackets):
                    s, x = process_packet(packet)
                    packet = s
                    subpacket_versions.append(x)
            if t_id == 0:
                return packet, sum(subpacket_versions)
            if t_id == 1:
                p = 1
                for x in subpacket_versions:
                    p *= x
                return packet, p
            if t_id == 2:
                return packet, min(subpacket_versions)
            if t_id == 3:
                return packet, max(subpacket_versions)
            if t_id == 5:
                return packet, 1 if subpacket_versions[0] > subpacket_versions[1] else 0
            if t_id == 6:
                return packet, 1 if subpacket_versions[0] < subpacket_versions[1] else 0
            if t_id == 7:
                return packet, 1 if subpacket_versions[0] == subpacket_versions[1] else 0

    result = process_packet(packet)

    return version_sum, result[1]


def main():
    with open("./2021/Day 16/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result1, result2 = part1(input_list)
    t1 = time.time()
    print(f"{result1}, {result2} is the result of part 1 and 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
