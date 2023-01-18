# Author ph
# Company NKCS
# created at 2023/1/18  9:19 AM

import os
import zipfile


# zip file to save space
def zip_files(path):
    DirName = os.path.dirname(path)
    BaseName = os.path.basename(path)
    pwd = os.getcwd()
    os.chdir(DirName)

    zipper = zipfile.ZipFile('temp.zip', 'w')
    if os.path.isdir(BaseName):
        for root, dirs, files in os.walk(BaseName):
            for name in files:
                path = os.path.join(root, name)
                zipper.write(path, compress_type=zipfile.ZIP_DEFLATED)
    else:
        zipper.write(BaseName, compress_type=zipfile.ZIP_DEFLATED)
    zipper.close()

    size = os.path.getsize('temp.zip')

    # faster than read bytes one by one
    with open('temp.zip', 'rb') as zipper:
        byteList = zipper.read()
    os.remove('temp.zip')
    os.chdir(pwd)

    return size, byteList


# only for text
def zip_input(content):
    with open('temp.txt', 'w') as file:
        file.write(content)
    path = os.path.join(os.getcwd(), 'temp.txt')

    size, byteList = zip_files(path)
    os.remove('temp.txt')

    return size, byteList


# generate a file that contains the info you hide from picture
def zip_write(byteList):
    byteStream = b''
    for byte in byteList:
        byteStream = byteStream + byte

    # faster than writing bytes one by one
    with open('temp.zip', 'wb') as zipper:
        zipper.write(byteStream)

    zipper = zipfile.ZipFile('temp.zip', 'r')
    zipper.extractall(os.getcwd())
    zipper.close()

    os.remove('temp.zip')
