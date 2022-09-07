import task_1


def is_equal_subnet(first_ip, third_id, mask) -> bool:
    return task_1.get_network_address(first_ip, mask) == task_1.get_network_address(third_id, mask)


if __name__ == '__main__':
    first_ip = list(map(int, input("input first ip:").split(".")))
    third_ip = list(map(int, input("input third ip:").split(".")))
    mask = list(map(int, input("input mask:").split(".")))

    # first_ip = list(map(int, "127.0.0.1".split(".")))
    # third_ip = list(map(int, "127.10.0.1".split(".")))
    # mask = list(map(int, "255.0.0.0".split(".")))

    print(is_equal_subnet(first_ip, third_ip, mask))
