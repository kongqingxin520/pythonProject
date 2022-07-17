password = 19950202
key = 6
print("原密码是：", password)
password = password << key
print("加密后的密码是：", password)
password = password >> key
print("揭秘后的密码是：%d" % password)
