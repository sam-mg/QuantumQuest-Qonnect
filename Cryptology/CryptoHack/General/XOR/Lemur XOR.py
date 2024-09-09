#!/usr/bin/env python3

from PIL import Image
from pwn import xor

lemur = Image.open('lemur.png')
flag = Image.open('flag.png')
Image.frombytes(flag.mode, flag.size, xor(lemur.tobytes(), flag.tobytes())).save('solve.png')
