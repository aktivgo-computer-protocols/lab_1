import const
import helper


def get_minimal_subnet_mask(first_ip: [], third_ip: []) -> list:
    mask = []
    count_equal_octets = get_count_equal_octets(first_ip, third_ip)
    for i in range(count_equal_octets):
        mask.append(const.BYTE_MAX_VALUE)

    mask.append(calculate_mask_byte(first_ip, third_ip, count_equal_octets))

    while len(mask) != const.IP_LENGTH:
        mask.append(0)

    return mask


# 127.0.0.1
# 127.2.0.1
# 255.254.0.0


def get_count_equal_octets(first_ip: [], third_ip: []) -> int:
    result = 0
    i = 0
    while first_ip[i] == third_ip[i]:
        result += 1
        i += 1
    return result


def calculate_mask_byte(first_ip: [], third_ip: [], byte: int) -> int:
    pointer = 128
    mask = 0

    while pointer & first_ip[byte] == pointer & third_ip[byte]:
        mask += pointer
        pointer >>= 1

    return mask


if __name__ == '__main__':
    first_ip = list(map(int, input("input first ip:").split(".")))
    third_ip = list(map(int, input("input third ip:").split(".")))

    # first_ip = list(map(int, "127.0.0.1".split(".")))
    # third_ip = list(map(int, "127.2.0.1".split(".")))

    # print("first_ip:", helper.ip_to_str(first_ip))
    # print("third_ip:", helper.ip_to_str(third_ip))

    print(helper.ip_to_str(get_minimal_subnet_mask(first_ip, third_ip)))
