#encoding:utf-8

def chineseToUnic(ch):
    return ch.decode('utf-8').encode('unicode_escape')
print chineseToUnic("你是猪")

print u'\u6211\u60f3\u4f60\u4e86'