from os.path import isfile

K = []
K += [0x5a827999] * 20
K += [0x6ed9eba1] * 20
K += [0x8f1bbcdc] * 20
K += [0xca62c1d6] * 20

H = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]

# 对信息分块 eg:  length = 23 return 1
#               length = 452 return 2
def count_blocks(length_of_messages):
    # 长度除以512 计算分块数 左移计算速度更快
    blocks = (length_of_messages >> 9)
    remainder = (length_of_messages - (blocks << 9))
    # print('余数: ', remainder)
    return (blocks + 1) if remainder < 448 else (blocks + 2)

def f(times, x, y, z):
    # python 3.10 替换
    # match times:
    #     case s if 0 <= s <= 19:
    #         return (x & y) ^ (~x & z)
    #     case s if 20 <= s <= 39 or 60 <= s <= 79:
    #         return x ^ y ^ z
    #     case s if 40 <= s <= 59:
    #         return (x & y) ^ (x & z) ^ (y & z)
    if times < 20:
        return (x & y) ^ (~x & z)
    elif times < 40:
        return x ^ y ^ z
    elif times < 60:
        return (x & y) ^ (x & z) ^ (y & z)
    else:
        return x ^ y ^ z

# python3.10才支持match...case，而且判断会影响速度，不如直接载入到内存
# def K(times):
#     match times:
#         case s if 0<=s<=19:
#             return 0x5a827999
#         case s if 20 <= s <= 39:
#             return 0x6ed9eba1
#         case s if 40 <= s <= 59:
#             return 0x8f1bbcdc
#         case s if 60 <= s <= 79:
#             return 0xca62c1d6

def sha1_file_sum():
    pass


def sha1_str_sum():
    pass


def sha1_result(sha1string):
    # 将文件和非文件转换为bytes类型
    if isfile(sha1string):
        with open(sha1string, 'rb') as f:
            file = f.read()
    else:
        sha1string = str(sha1string)
    byteMessage = sha1string.encode()
    lengthOfMessages = len(byteMessage) * 8
    # 文本分块
    blockNumber = count_blocks(lengthOfMessages)
    # 补位
    byteMessage += b'\x80'
    zeroBits = (blockNumber * 512 - 64 - 8 - lengthOfMessages)
    byteMessage += b'\x00' * (zeroBits // 8)
    byteMessage += lengthOfMessages.to_bytes(8, byteorder='big')

    for block in range(0, blockNumber):
        W = []
        for t in range(0, 80):
            if t < 16:
                W.append(int.from_bytes(byteMessage[(block * 64 + t * 4): ((block * 64) + (t + 1) * 4)]))
            else:
                W_temp = W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16]
                W.append((W_temp << 1 | W_temp >> 31) & 0xffffffff)
        a = H[0]
        b = H[1]
        c = H[2]
        d = H[3]
        e = H[4]
        # 每块进行80轮计算
        for t in range(0, 80):
            T = (((a << 5) | (a >> 27)) + f(t, b, c, d) + e + K[t] + W[t]) & 0xffffffff
            e = d
            d = c
            c = (b << 30 | b >> 2) & 0xffffffff
            b = a
            a = T
        H[0] = (a + H[0]) & 0xffffffff
        H[1] = (b + H[1]) & 0xffffffff
        H[2] = (c + H[2]) & 0xffffffff
        H[3] = (d + H[3]) & 0xffffffff
        H[4] = (e + H[4]) & 0xffffffff

    SHA1 = f"{H[0]:08x}{H[1]:08x}{H[2]:08x}{H[3]:08x}{H[4]:08x}"
    return SHA1