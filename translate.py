import sys, os
from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook
from openpyxl.cell import coordinate_from_string, column_index_from_string
from datetime import datetime


#check if running with python3
if sys.version_info[0] < 3:
    raise "Must be using Python 3"

# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

if len(sys.argv) < 2 :
    print('Error: No input')
    sys.exit(0)

#load excel file
filename = sys.argv[1]
wb = load_workbook(filename = filename)
sheet = wb.active 

englishColumnIndex = 'A'
if len(sys.argv) > 2 :
    englishColumnIndex = sys.argv[2]
print('English column index:' + englishColumnIndex)

ignore_row_number = 0
if len(sys.argv) > 3:
    ignore_row_number = int(sys.argv[3])
print('ignore_row_number:' + str(ignore_row_number))

ignore_column_number = 0
if len(sys.argv) > 4:
    ignore_column_number = int(sys.argv[4])
print('ignore_column_number:' + str(ignore_column_number))

#get folder path
folder = os.path.dirname(os.path.abspath(filename))
print('file folder: '+ folder)

#read row and column
row_count = sheet.get_highest_row() 
column_count = sheet.get_highest_column()
invalid_cell_count = 0

# print ('File: ' + filename  + " -> " + str(row_count) + " rows and " + str(sheet.get_highest_column()) + " columns")

for col in sheet.columns: 
    targetLanguageColumn = col[0].column
    if sheet[ str(targetLanguageColumn+'1') ].value:    #check if there is a language name (avoid empty)
        outputFilename = sheet[ str(targetLanguageColumn+'1') ].value +'.strings'
        outputFolder = folder + '/'+filename+'-output/'
        if not os.path.exists(outputFolder):
            os.makedirs(outputFolder)

        dotStringFile = open(outputFolder + outputFilename, 'w', encoding='utf8')
        print('Generating: ' + outputFolder + outputFilename)

        fileContent = '/* Auto generated .string file from EXCEL with Python script. \nAuthor: raxcat@github \nCopyright: raxcat@github 2015 \nTimestamp:'+ str(datetime.now())+'*/\n\n'

        for cell in col:
            if cell.value :  #check if there is any value(not empty cell)
                if cell.row > ignore_row_number and column_index_from_string(cell.column) >  ignore_column_number: #check ignore row and column
                    languageIndex = str(cell.column)+"1"
                    language = (str(sheet[languageIndex].value)).strip()

                    # print ( '[' + str(cell.column)+str(cell.row)+']'  + '(' +language + ')')

                    englishContentIndex = englishColumnIndex + str(cell.row)
                    englishContent = (str(sheet[englishContentIndex].value)).rstrip()   #string due to some err in excel
                    translatedContent = str(cell.value).rstrip()

                    line1 = '/* '+ '(' + language + ')' + ' Auto translation of word: ' + '"' + englishContent + '"'+' */'
                    line2 = '"'+englishContent + '" = "' + translatedContent + '";'

                    # print(line1)
                    # print(line2)
                    # print('')

                    fileContent += line1+'\n'
                    fileContent += line2+'\n'
                    fileContent += ('\n')
            else:
                invalid_cell_count += 1

        dotStringFile.write(fileContent)
    else:
        invalid_cell_count += 1

print('There are ' + str(invalid_cell_count) + ' empty cells in raw excel file')