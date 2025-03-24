a = 123.123
b = bytearray(str(a).encode())
b.append(0b1011)
print(len(b))
print(b)