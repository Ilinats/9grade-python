#Преименувайте файл (през код-а)

import os

old_name = r"C:\Users\kniag\Documents\TUES\9ti_klas\vuvedenie v skriptovite ezici\files\rename.txt"
new_name = r"C:\Users\kniag\Documents\TUES\9ti_klas\vuvedenie v skriptovite ezici\files\rename1.txt"

os.rename(old_name, new_name)