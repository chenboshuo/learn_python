# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# *Humans use text. Computers speak bytes*
#
# *-- Ester Nam and Travis Fischer*

# # Texts verus Bytes
#

# ## Character Issues
# The Unicode standard explicity seprates the identity of character
# from specific byte representations:
# 1. The identity of a character --ites code point
# -- is a number from `0` to `1,114,111`(base 10),
# shown in Unicode standard as 4 to 6 hexadecimal digits with a "U+" prefix.
# For example, the code point for the letter `A` is `U+0041`.
# About 10% of the valid code points have chatacters assigned to them in Unicode 6.4,
# the standard used in python 3.5
# 2. the actual bytes that present a chatacter depend on the encoding in use.

s = 'A'
s.encode('utf8') # Encode str to bytes using UTF-8 encoding

b'\x41'

s = '你好'
len(s)

len(s.encode('utf8'))

len('a'.encode('utf8'))

len('é'.encode('utf8'))

# ## Byte Essentials

# The immutable bytes types introduced in python 3 and the mutable `bytearray`,
# added in python 2.6.

cafe = bytes('café', encoding='utf_8') # bytes can be built from str, given an encoding
cafe

cafe[0] # Each item is an integer inn range(256)

cafe[:1] # Slice of bytes are also bytes--even slices of a single byte

# Although binary sequence are really sequences of integers, their literal notation reflects the fact
# that `ASCII` text is often embedded in them.

# Binary sequences have a class method that `str` doesn't have called `fromhex`,
# which builds a binary sequence by parsing of hex digits optionally sparated by space

bytes.fromhex('31 4b CE A9')

import array
numbers = array.array('h', [-2, -1, 0, 1, 2]) # Type code 'h' creates an array of short integers(16bits)
octets = bytes(numbers)
octets # These are 10 bytes that represent the five short integers

list(octets)

# ## Basic Encoders/Decoders

for codec in ['utf8', 'utf16', 'gbk']:
    print(codec, 'café hello 中文'.encode(codec),sep='\t')


