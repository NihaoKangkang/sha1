def hex_encode(messages):
    return int(messages.encode().hex(), 16)


# 对信息分块 eg:  length = 23 return 1
#               length = 452 return 2
def count_blocks(length_of_messages):
    # 长度除以512 计算分块数 左移计算速度更快
    blocks = (length_of_messages >> 9)
    remainder = (length_of_messages - (blocks << 9))
    print(remainder)
    return (blocks + 1) if remainder <= 448 else (blocks + 2)


# 输入字符串
message = 'abc'

# 转化为16进制
hexMessage = hex_encode(message)

# 计算字符串长度 向上取整计算byte
lengthOfMessages = ((hexMessage.bit_length() + 8 - 1) >> 3) << 3
print('length of bits: ', lengthOfMessages)

# 分块
blockNumber = count_blocks(lengthOfMessages)
# blockNumber = count_blocks(1000)
print('blocks: ', blockNumber)

# 补零

