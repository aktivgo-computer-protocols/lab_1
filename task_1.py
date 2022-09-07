import const
import helper


def get_network_address(ip, mask) -> list:
    network_address = []
    for i in range(const.IP_LENGTH):
        network_address.append(ip[i] & mask[i])
    return network_address


def get_node_address(ip, mask) -> list:
    node_address = []
    for i in range(const.IP_LENGTH):
        node_address.append(ip[i] & (const.BYTE_MAX_VALUE - mask[i]))
    return node_address


def get_count_nodes(mask) -> int:
    degree = 0
    i = 0

    while mask[i] == const.BYTE_MAX_VALUE and i < const.BYTE_MAX_VALUE:
        i += 1

    degree += bin(mask[i]).count("0") - 1

    while i != const.IP_LENGTH - 1:
        degree += const.BIT_IN_BYTE
        i += 1

    return 2 ** degree - 2


def get_broadcast_address(network_address, mask) -> list:
    broadcast_address = network_address
    inverted_mask = get_invert_ip(mask)
    for i in range(const.IP_LENGTH):
        if mask[i] != const.BYTE_MAX_VALUE:
            broadcast_address[i] = network_address[i] + inverted_mask[i]

    return broadcast_address


def get_invert_ip(ip: []) -> list:
    result = []
    for i in range(const.IP_LENGTH):
        result.append(const.BYTE_MAX_VALUE - ip[i])
    return result


def print_ip_info(ip: [], mask: []) -> None:
    network_address = get_network_address(ip, mask)
    print("ip address of network:", helper.ip_to_str(network_address))

    node_address = get_node_address(ip, mask)
    print("ip address of node:", helper.ip_to_str(node_address))

    count_nodes = get_count_nodes(mask)
    print("nodes count in network:", count_nodes)

    broadcast_address = get_broadcast_address(network_address, mask)
    print("broadcast address:", helper.ip_to_str(broadcast_address))


if __name__ == '__main__':
    ip = list(map(int, input("input first ip:").split(".")))
    mask = list(map(int, input("input mask:").split(".")))

    # ip = list(map(int, "127.0.0.1".split(".")))
    # mask = list(map(int, "255.128.0.0".split(".")))
    #
    # print("ip:", helper.ip_to_str(ip))
    # print("mask:", helper.ip_to_str(mask))

    print_ip_info(ip, mask)
