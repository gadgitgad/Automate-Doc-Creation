from openpyxl import load_workbook
import os
import re

# Extract all title of PTS for <New feature>
os.chdir("C:\\Users\\HP\\Documents\\Project_GitHUB_Doc_Automation\\Doc_Store")
wb=load_workbook(filename="STM32CubeProgrammer_for TPC_SFI OB CSV Generation GUI_Verif&Valid_PTS_Product_Test_Specification.xlsx")
name_sheet=wb['Identification']
print(name_sheet['B3'].value)
title=name_sheet['B3'].value
print(type(title))
# Extract info from title
x=title.split("for",1)
print(x)
feature_name=x[1]
print(feature_name)