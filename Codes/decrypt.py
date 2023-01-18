# Author ph
# Company NKCS
# created at 2023/1/17  8:40 PM

import cv2
from zipper import zip_write


def parseHeader(img, col):
    size = 0
    for i in range(32):
        x = int(i / col)
        y = int(i % col)
        size = size * 2
        size = size + (img[x][y][0] & 1)
    return size


def parseData(img, col):
    size = parseHeader(img, col)

    bitList = []
    for i in range(32, 32 + size * 8):
        x = int(i / col)
        y = int(i % col)
        bitList.append(img[x][y][0] & 1)

    byte = 0
    byteList = []
    for i in range(size * 8):
        byte = byte << 1
        byte = byte + bitList[i]
        if (i + 1) % 8 == 0:
            byteList.append(int(byte).to_bytes(1, 'big'))
            byte = 0

    return byteList


def parseImage(path):
    img = cv2.imread(path)
    row, col, channel = img.shape

    byteList = parseData(img, col)
    zip_write(byteList)


if __name__ == '__main__':
    parseImage('./src/newimg.png')


