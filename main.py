from os.path import isfile

from SHA import *

# 输入字符串
# inputMessage = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz123'
# inputMessage = 'abc'
# inputMessage = "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
# inputMessage = 'a' * 1000000
inputMessage = str(123.123)
file_path = './binfile.bin'
isfile(file_path)
# with open(file_path, 'rb') as f:
#     binary_read = f.read(512)
#
#     print()
print(isfile('123123'))
# padding = bytearray(emessage)

# padding.append(0b10000000)
# pop bytes
# padding.pop(-1)

# print(type(padding))
# print('bytearray: ',padding)
# print(type(bytes(padding).decode()))
# print('bytes to string: ',bytes(padding).decode())

# 转化为字节流
# byteMessage = inputMessage.encode()
# # hexMessage = int(byteMessage.hex(), 16)
# # 计算字符串长度 向上取整计算byte
# lengthOfMessages = len(byteMessage) * 8
# # 448bits边界测试
# # lengthOfMessages = 56 * 8
# # print('length of bits: ', lengthOfMessages)
#
# # 分块
# blockNumber = count_blocks(lengthOfMessages)
# # blockNumber = count_blocks(1000)
# # print('blocks: ', blockNumber)
#
# # 补位，如果bit流需要修改这里
# # 首位补1 其余补0
# byteMessage += b'\x80'
# zeroBits = (blockNumber * 512 - 64 - 8 - lengthOfMessages)
# byteMessage += b'\x00' * (zeroBits // 8)
# # 补长度 需要把长度变为16进制
# # 输出长度为8bytes，大端在前的64bits消息长度
# byteMessage += lengthOfMessages.to_bytes(8, byteorder='big')
# # print('byteMessage: ', byteMessage)
# for block in range(0, blockNumber):
#     W = []
#     for t in range(0, 80):
#         if t < 16:
#             W.append(int.from_bytes(byteMessage[(block * 64 + t * 4): ((block * 64) + (t + 1) * 4)]))
#             # print(f"W[{t}] = {hex(W[t])}")
#         else:
#             W_temp = W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16]
#             W.append((W_temp << 1 | W_temp >> 31) & 0xffffffff)
#     # for i in range(0, 80):
#     #     print(hex(W[i]) ,end=' ')
#     #     if (i + 1) % 4 == 0:
#     #         print()
#     # print()
#     a = H[0]
#     b = H[1]
#     c = H[2]
#     d = H[3]
#     e = H[4]
#     # 每块进行80轮计算
#     for t in range(0,80):
#         # python 3.10 替换
#         # T = (((a << 5)|(a >> 27)) + f(t, b, c, d) + e + K(t) + W[t]) & 0xffffffff
#         T = (((a << 5) | (a >> 27)) + f(t, b, c, d) + e + K[t] + W[t]) & 0xffffffff
#         e = d
#         d = c
#         c = (b << 30 | b >> 2) & 0xffffffff
#         b = a
#         a = T
#         # print('t=', t, ': ', f"{a:08x}", '\t\t', f"{b:08x}", '\t\t', f"{c:08x}", '\t\t', f"{d:08x}", '\t\t', f"{e:08x}")
#     H[0] = (a + H[0]) & 0xffffffff
#     H[1] = (b + H[1]) & 0xffffffff
#     H[2] = (c + H[2]) & 0xffffffff
#     H[3] = (d + H[3]) & 0xffffffff
#     H[4] = (e + H[4]) & 0xffffffff
#
# SHA1 = f"{H[0]:08x}{H[1]:08x}{H[2]:08x}{H[3]:08x}{H[4]:08x}"

print('SHA-1: ', sha1_result(inputMessage))

