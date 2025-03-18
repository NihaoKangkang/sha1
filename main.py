# 愿景： 设计一个支持bit流sha1加密软件，先做byte流

# 对信息分块 eg:  length = 23 return 1
#               length = 452 return 2
def count_blocks(length_of_messages):
    # 长度除以512 计算分块数 左移计算速度更快
    blocks = (length_of_messages >> 9)
    remainder = (length_of_messages - (blocks << 9))
    print('余数: ', remainder)
    return (blocks + 1) if remainder < 448 else (blocks + 2)

H = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]

# 输入字符串
# inputMessage = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz123'
inputMessage = 'abc'
# padding = bytearray(emessage)

# padding.append(0b10000000)
# pop bytes
# padding.pop(-1)

# print(type(padding))
# print('bytearray: ',padding)
# print(type(bytes(padding).decode()))
# print('bytes to string: ',bytes(padding).decode())

# 转化为字节流
byteMessage = inputMessage.encode()
# hexMessage = int(byteMessage.hex(), 16)
# 计算字符串长度 向上取整计算byte
lengthOfMessages = len(byteMessage) * 8
# 448bits边界测试
# lengthOfMessages = 56 * 8
print('length of bits: ', lengthOfMessages)

# 分块
blockNumber = count_blocks(lengthOfMessages)
# blockNumber = count_blocks(1000)
print('blocks: ', blockNumber)

# 补位，如果bit流需要修改这里
# 首位补1 其余补0
byteMessage += b'\x80'
zeroBits = (blockNumber * 512 - 64 - 8 - lengthOfMessages)
byteMessage += b'\x00' * (zeroBits // 8)
# 补长度 需要把长度变为16进制
# 输出长度为8bytes，大端在前的64bits消息长度
byteMessage += lengthOfMessages.to_bytes(8, byteorder='big')

W = []
for t in range(0, 79):
    if t < 16:
        W.append(int.from_bytes(byteMessage[ t * 4 : ( t + 1 ) * 4 ]))
    else:
        W.append(W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16] << 1)

# print W
# for i in range(0, 79):
#     print(hex(W[i]) ,end=' ')
#     if (i + 1) % 4 == 0:
#         print()
# print()
for t in range(0, blockNumber):
    a = H[0], b = H[1], c = H[2], d = H[3], e = H[4]
    H[0] = a + H[0] >> 32 
print(byteMessage)

