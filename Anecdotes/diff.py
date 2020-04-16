import re

def canonize(text):
    reg = re.compile('[a-zA-Zа-яА-Я]+')
    return [x for x in reg.findall(text.lower()) if len(x) > 2]


def gen_shingle(source, length=4):
    import binascii
    if len(source) < length:
        source += ["any"] * (length - len(source))
    # out = []
    # for i in range(len(source)-(length - 1)):
    #     out.append(binascii.crc32(' '.join([x for x in source[i:i + length]]).encode('utf-8')))

    return [binascii.crc32(' '.join([x for x in source[i:i + length]]).encode('utf-8')) for i in range(len(source)-length + 1)]


def compare(source1, source2):
    same = 0
    for i in range(len(source1)):
        if source1[i] in source2:
            same = same + 1
    return same*2/float(len(source1) + len(source2))*100


def compare_text(text1, text2):
    k = 2  # Will assume if lengthes of  texts after canonization differ more then k times then
    # texts are different
    x1 = canonize(text1)
    x2 = canonize(text2)
    if len(x1) > k * len(x2) or len(x2) > k * len(x1):
        return False
    shinglelen = min(4, len(x1), len(x2))
    return compare(gen_shingle(x1, shinglelen), gen_shingle(x2, shinglelen)) > 0

def _checkDB(self):
    #
    # Looking for dublicates
    #
    all = self.data.getall()
    dublicates = [(i['id'], k['id']) for i in all for k in all if i['id'] > k['id']
                  and diff.compareText(i['anecdote'], k['anecdote'])]
    if len(dublicates) > 0:
        self.after_check = True
        print(dublicates)
        self.lst = list(chain.from_iterable(dublicates))
        self._build_listbox()



if __name__ == '__main__':
    file1 = "text1.txt"
    encod = "cp1251"
    with open(file1, encoding=encod) as txt1:
        try:
            ttt1 = txt1.read()
        except UnicodeDecodeError as e:
            print(e.encoding)
            print(e.reason)
            print(e.object)
            print(e.start)
            print(e.end)

    file2 = "text2.txt"
    with open(file2, encoding=encod) as txt2:
        ttt2 = txt2.read()

    x1 = canonize(ttt1)
    x2 = canonize(ttt2)
    y1 = gen_shingle(x1, 3)
    y2 = gen_shingle(x2, 3)
    print(x1, x2)
    print(y1, y2)
    print(compare(x1, x2))
    print(compare(y1, y2))
