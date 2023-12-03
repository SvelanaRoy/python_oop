datalist = []
def readfilelines(file):
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
        datalist.append((len(lines),lines,file))

readfilelines("1.txt")
readfilelines("2.txt")
readfilelines("3.txt")
countdatalist = len(datalist)
count = 0
with open('union.txt', 'a', encoding="utf-8") as fp:
    for text in sorted(datalist, key=lambda text: text[0]):
        fp.writelines(f"{text[2]}\n{text[0]}\n")
        fp.writelines(text[1])
        count += 1
        if count < countdatalist:
            fp.writelines("\n")

