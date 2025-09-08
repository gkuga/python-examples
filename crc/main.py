# CRC-16 calulation in Python

def calc_crc(data: bytes) -> int:
    # 1. Initialize CRC to 0xFFFF
    crc = 0xFFFF
    for b in data:
        # 2. XOR the byte into the CRC
        crc ^= b
        # 3. Process each bit of the byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    # 4. Return the CRC value, swapping the bytes
    return ((crc >> 8) & 0xFF) | ((crc & 0xFF) << 8)


# CRC Target Data
data = bytes([0x02, 0xa1, 0x00])

crc = calc_crc(data)

print(f"CRC (hex): {crc:04x}")  # Expects a9 90
