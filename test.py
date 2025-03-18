test = b'abc\x80'
test2 = bytearray(test)
test2.append(0)
test2.append(0x33)
print(test2)