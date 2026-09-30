def is_valid_part(part):
    try:
        i_part = int(part)
        if part[0] == '0' and not i_part == 0: return False
        return 0 <= i_part < 256
    except ValueError as ve:
        return False

def is_valid_ip(ip: str):
    parts = ip.split('.')
    if len(parts) != 4: return False
    for part in parts:
        if not is_valid_part(part): return False
    return True

# print( is_valid_part('127'), is_valid_part('AAA'), is_valid_part('257'), is_valid_part('-255'), is_valid_part('01'), is_valid_part('0')

print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False