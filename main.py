import re

import openpyxl

FILENAME = "СНИЛС.xlsx"

wb_obj_1 = openpyxl.load_workbook(FILENAME)
sheet1 = wb_obj_1.active
mass = []
for row in sheet1.iter_rows():
    mass.append(row[0].value)

for snils in mass:
    try:
        snils = re.sub(r"[^\d]", "", snils)
    except:
        pass
    number = snils[:9]
    check = snils[-2:]
    checksum = 0
    pl = 9
    for num in number:
        checksum += int(num)*pl
        pl-= 1
    if checksum > 101:
        checksum = checksum % 101
    if checksum == 100 or checksum == 101:
        checksum = 0
    if int(checksum) == int(check):
        print(str(snils) + " is valid")
    else:
        print(str(snils) + " INVALID")

