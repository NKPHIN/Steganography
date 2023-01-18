# Author ph
# Company NKCS
# created at 2023/1/17  6:22 PM
import os

import cv2
from zipper import zip_files, zip_input


# init a 32bit header contains the size of data
def initHeader(size):
    header = []
    while size:
        bit = int(size) % 2
        size = int(size) / 2
        header.append(bit)
    for i in range(32 - len(header)):
        header.append(0)

    return header


# convert byte to bits
def byte2bit(byteList):
    bitList = []
    for byte in byteList:
        for i in range(7, -1, -1):
            if byte >> i & 1:
                bitList.append(1)
            else:
                bitList.append(0)
    return bitList


# encrypt a file
def encrypt_file(src, dst):
    """
    :param src: the file you want to hide from a picture
    :param dst: the picture used to hide a file
    :return: None
    """
    size, byteList = zip_files(src)
    generate_PNG(size, byteList, dst)


# encrypt the standard input
def encrypt_input(content, dst):
    """
    :param content: the content you want to hide from picture
    :param dst: the picture used to hide a file
    :return: None
    """
    size, byteList = zip_input(content)
    generate_PNG(size, byteList, dst)


# generate a picture(.png) which hidden info
# you can also generate .bmp
def generate_PNG(size, byteList, dst):
    img = cv2.imread(dst, cv2.IMREAD_COLOR)
    row, col, channel = img.shape

    if int(row * col / 8) < size + 4:
        print('内容超过图片限制!')
        return

    bitList = byte2bit(byteList)
    header = initHeader(size)

    for i in range(32):
        x = int(i / col)
        y = int(i % col)
        # make the lowest bit of img[x][y][0] to 0
        # then add header[31-i], which is 0 or 1
        img[x][y][0] = (img[x][y][0] & 254) + header[31 - i]

    for i in range(32, 32 + size * 8):
        x = int(i / col)
        y = int(i % col)
        img[x][y][0] = (img[x][y][0] & 254) + bitList[i - 32]

    cv2.imwrite('./src/newimg.png', img)


if __name__ == '__main__':
    # encrypt_file('./src/test.txt', './src/test.jpeg')
    encrypt_input('These violent delights have violent ends.', './src/test.jpeg')
