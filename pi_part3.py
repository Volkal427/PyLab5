def is_valid_part(part):
    try:
        i_part = int(part)
        if part[0] == '0' and not i_part == 0:
            return False
        return 0 <= i_part < 256
    except ValueError:
        return False


def is_valid_ip(ip):
    parts = ip.split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not is_valid_part(part):
            return False

    return True


def decimal_to_binary(n):
    if n == 0:
        return '0'

    if n == 1:
        return '1'

    next, digit = divmod(n, 2)

    return decimal_to_binary(next) + str(digit)


def binary_to_decimal(b):
    if b == '':
        return 0

    place = len(b) - 1

    return 2**place * int(b[0]) + binary_to_decimal(b.removeprefix(b[0]))


# Part 1

def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return "Invalid IP address"

    parts = ip.split('.')
    answer = ""

    for part in parts:
        binary = decimal_to_binary(int(part))

        while len(binary) < 8:
            binary = "0" + binary

        answer += binary + "."

    return answer[:-1]


# Part 2

def binary_to_ip(ip):
    parts = ip.split('.')

    if len(parts) != 4:
        return "Invalid IP address"

    answer = ""

    for part in parts:
        if len(part) != 8:
            return "Invalid IP address"

        for digit in part:
            if digit != '0' and digit != '1':
                return "Invalid IP address"

        decimal = binary_to_decimal(part)
        answer += str(decimal) + "."

    return answer[:-1]


def ip_convert(ip):
    parts = ip.split('.')

    if len(parts) != 4:
        return "Invalid IP address"

    binary = True

    for part in parts:
        if len(part) != 8:
            binary = False

    if binary:
        return binary_to_ip(ip)
    else:
        return ip_to_binary(ip)

# Part 1 test
# print(ip_to_binary("192.168.1.1"))
# print(ip_to_binary("255.255.255.0"))
# print(ip_to_binary("256.1.1.1"))

#Part 2 test
# print(binary_to_ip("11000000.10101000.00000001.00000001"))
# print(ip_convert("192.168.1.1"))
# print(ip_convert("11000000.10101000.00000001.00000001"))