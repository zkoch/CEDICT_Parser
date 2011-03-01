CC-CEDICT is an English Chinese dictionary freely available for use in applications and other such things. It can be downloaded here: http://www.mdbg.net/chindict/chindict.php?page=cc-cedict

The dictionary contains around 100k lines, and they all follow the same order:

TRADITIONAL_CHARS SIMPLIFIED_CHARS [PINYIN] /DEF 1/DEF 2

The biggest issue with this dictionary, however, is that the pinyin comes in the form: zhong1 guo2. That's not all that helpful for people, so we need to convert those into letters with actual tones marks:  Zhōngguó

This code was originally writhed for use in converting the dictionary into a JS object for use in another project, but you should be able to extract what you need for your own purposes.

File Overview:

pinyin.py -> Within is a method that takes a string of pinyin and tone marks (e.g. zhong1 guo2) and converts to actual tone marks

parser.py -> Reads the dictionary, parses out the simplified chars, pinyin, and definitions, uses pinyin.py to convert the pinyin, and then puts the resulting dictionaries into an array.

GOALS:

- write cleaner code
- genericize it so people can use it easily
- do some command line wizardry maybe