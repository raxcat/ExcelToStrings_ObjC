# ExcelToStrings_ObjC
This project demonstrates how to use a simply python script to convert a multi-language excel file to Objective-C .strings files. Lots of developers who do not use English as there native language and they may have to do some i18n jobs, receiving excel file from professional translators. This project helps to convert these kinds of excels to Objective-C .strings files in secs.

#Requirements
- Python3
- [Openpyxl] - Python package that eads and writes from xlsx
- Translated excel files.
    - Row -> Each word item
    - Column -> Language

#Note
I am not a pro python programmer, this script just works but not good enough. Please advise if you have any suggestion.

#Environment
This script has been tested under Mac OS 10.10.3 with python2 and python3 installed, running py with python3.

#Usage
**Command definition**
```sh
$ python3 filename [EnglishColumnIndex] [IgnoreRowNumber] [IgnoreColNumber]
```

####Example1
Only filename, deault EnglishColumnIndex would be `A`, dafault IgnoreRowNumbers would be `0`, and default IgnoreColumnNumber would be `0` 
```bash
$ python3 translate.py example1.xlsx
```
![Alt text](/example1.png?raw=true "Optional title")
And you wiil get output like this
```bash
$ English column index:A
$ ignore_row_number:0
$ ignore_column_number:0
$ file folder: /Users/raxcat/translation
$ Generating: /Users/raxcat/translation/AMCommon.xlsx-output/Englsih.strings
$ Generating: /Users/raxcat/translation/AMCommon.xlsx-output/繁体中文.strings
$ Generating: /Users/raxcat/translation/AMCommon.xlsx-output/简体中文.strings
$ Generating: /Users/raxcat/translation/AMCommon.xlsx-output/日本語.strings
$ ...(ignored)
$ There are 42 empty cells in raw excel file
```

####Example2
Specifying filename, EnglishColumnIndex to `B`, dafault IgnoreRowNumbers would be `2`, and default IgnoreColumnNumber to `1` 
```bash
$ python3 translate.py example2.xlsx B 2 1
```
![Alt text](/example2.png?raw=true "Optional title")
```bash
$ English column index:B
$ ignore_row_number:2
$ ignore_column_number:1
$ file folder: /Users/brian/Downloads/python translation
$ Generating: /Users/brian/Downloads/python translation/AMCommon.xlsx-output/Englsih.strings
$ Generating: /Users/brian/Downloads/python translation/AMCommon.xlsx-output/繁体中文.strings
$ Generating: /Users/brian/Downloads/python translation/AMCommon.xlsx-output/简体中文.strings
$ Generating: /Users/brian/Downloads/python translation/AMCommon.xlsx-output/日本語.strings
$ Generating: /Users/brian/Downloads/python translation/AMCommon.xlsx-output/韩语.strings
$ Generating: /Users/brian/Downloads/python translation/AMCommon.xlsx-output/意大利语.strings
$ Generating: /Users/brian/Downloads/python translation/AMCommon.xlsx-output/捷克语.strings
$ ...(ignored)
$ There are 142 empty cells in raw excel file
```

####Result
![Alt text](/result.png?raw=true "Optional title")

#Feature works
- Test compatibility for xls file. (Older excel file format)
- Test compatibility on other OS platforms. (Only MacOSX is tested)

#Credit
Project inspired by **@SplendetWang[https://github.com/Splendent]**'s python script.

[Openpyxl]:https://openpyxl.readthedocs.org/en/latest/index.html
