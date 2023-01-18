# Steganography
Hide files in picture via LSB

## principe
   Stores hidden info using the lowest bit of the R channel of the image pixel. Since the pixel value does not change by more than 1, it is difficult for the human eye to distinguish the difference before and after the change, thus hiding the info.

## zipper
   Compression of the file or input to be processed in order to hide more info in the image

## encrypt
   The first 32 pixels of the image store the header, which records the length of the info to be hidden (in bytes), it is sufficient for most files

   From the 33rd pixel, the image stores each bit of the info to be hidden in order

## decrypt
   The hidden message is parsed backwards according to the encrypt encoding

## Storage size
   For example, if the image size is 1024 * 640, a total of 1024 * 640 / 8 / 1024 = 80K bytes can be stored, which is sufficient for most information.

