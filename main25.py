# Sec 25: Student Project - Text files to pdf

import pandas as pd
# to generate pdf file
from fpdf import FPDF

# to get the path of the files with certain extension
import glob

# to remove extensions of the file name
from pathlib import Path

# create an object fpdf from Class FPDF
pdf = FPDF(orientation="P", unit="mm", format="A4")


# get the file paths of all the text files and store it in a variable
filepaths = glob.glob("txt/*.txt")
print(filepaths)


for filepath in filepaths:
    pdf.add_page()  # add a page in pdf file
    pdf.set_font(family="Times", style="B", size=18)  # set the font settings
    pdf.set_text_color(0,0,0)  # set the color settings
    # remove the extension from the filepaths and capitalize the 1st letter of the file name
    filetopic= Path(filepath).stem.title()
    print(filetopic)
    pdf.cell(w=0, h=14 , align="L",txt=filetopic,ln=1 , border=0)

# generate pdf file (the pdf file should contain 4 pages , each file name as title on  a separate page)
pdf.output("PDF/animals.pdf")