# About

A script to convert Chinese folder names to pinyin. revised according to: http://sunzhen.blogspot.com/2016/05/rename-chinese-filenames-to-pinyin.html


## Setup

This script converts all file and folder names in the sub folder "data" into Pinyin.

If different unicode maps to the same pinyin such as "利" and "立"" both map to "li" and 1 will be added to the filename.

Tested with Python 3.6 via virtual environment:
```shell
$ python3.6 -m venv venv
$ source venv/bin/activate
$ python ch-to-pinyin.py
```

## An Example

Before:

<img width="1391" alt="Screen Shot 2019-09-24 at 11 43 08 AM" src="https://user-images.githubusercontent.com/595772/65527394-91a35b80-dec0-11e9-8df3-f54f76a2a77e.png">

After:

<img width="1394" alt="Screen Shot 2019-09-24 at 11 43 20 AM" src="https://user-images.githubusercontent.com/595772/65527400-936d1f00-dec0-11e9-8e42-4126839b9342.png">
