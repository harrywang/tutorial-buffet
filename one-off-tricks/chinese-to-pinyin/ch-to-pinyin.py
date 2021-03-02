# renameCH2Pinyin.py
# Rename filename from Chinese characters to capitalized pinyin using the
# mapping file and taking out the tone numbers

import os
import re

# File uni2pinyin is a mapping from hex to Pinyin with a tone number
f = open('uni2pinyin')
wf = f.read() # read the whole mapping file

os.chdir('data') # to rename all files in sub folder 'voc'
filename_list = os.listdir(u'.') # read all file names in unicode mode
print(filename_list)
for filename_unicode in filename_list: # each file name
    filename_pinyin = ''
    for c in filename_unicode: # each character
        if 0x4e00 <= ord(c) <= 0x9fff: # Chinese Character Unicode range
            hexCH = (hex(ord(c))[2:]).upper() # strip leading '0x' and change
                                              # to uppercase
            p = re.compile(hexCH+'\t([a-z]+)[\d]*') # define the match pattern
            mp = p.search(wf)
            filename_pinyin+=mp.group(1).title() # get the pinyin without the tone
                                            # number and capitalize it
        else:
            filename_pinyin+=c
    print(filename_unicode, filename_pinyin)

    latest_filename_list = os.listdir(u'.')
    while filename_pinyin in latest_filename_list:
        filename_pinyin= filename_pinyin + '1'
        print(filename_pinyin)
    os.rename(filename_unicode, filename_pinyin)
os.chdir('..') # go back to the parent folder
