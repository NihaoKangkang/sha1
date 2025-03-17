# 愿景： 设计一个支持bit流sha1加密软件，先做byte流

# 对信息分块 eg:  length = 23 return 1
#               length = 452 return 2
def count_blocks(length_of_messages):
    # 长度除以512 计算分块数 左移计算速度更快
    blocks = (length_of_messages >> 9)
    remainder = (length_of_messages - (blocks << 9))
    print('余数: ', remainder)
    return (blocks + 1) if remainder < 448 else (blocks + 2)


# 输入字符串
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
# lengthOfMessages = 55 * 8
print('length of bits: ', lengthOfMessages)

# 补位，如果bit流需要修改这里
# 其实知道lengthOfMessages可以优化这里
byteMessage += b'\x80'
if (len(byteMessage) % 64 != 56):
    pass

# 分块
blockNumber = count_blocks(lengthOfMessages)
# blockNumber = count_blocks(1000)
print('blocks: ', blockNumber)

# 补零

