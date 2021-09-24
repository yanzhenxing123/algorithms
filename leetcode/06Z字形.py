def convert(str1, num):
    if num == 1:
        return str1
    row = num
    length = len(str1)
    col = 0
    if (num != 2):
        while (length > 0):
            if (col % 2 == 0):
                length -= row
                col += 1
            else:
                length = length - row + 2
                col += 1
    else:
        col = int((length+1)/2)
    li = [[''] * col for _ in range(row)]
    index = 0
    for i in range(col):
        if (i % 2 == 0 or num == 2):
            for j in range(row):
                if (index < len(str1)):
                    li[j][i] = str1[index]
                    index += 1
        else:
            for j in range(row-2, 0, -1):
                if (index < len(str1)):
                    li[j][i] = str1[index]
                    index += 1

    str2 = ""
    for i in range(row):
        for j in range(col):
            str2 += li[i][j]
    return str2


if __name__ == '__main__':
    str1 = "LEETCODEISHIRING"
    convert(str1, 4)
