# Sec 25: Student Project - Text files to pdf

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
    # remove the extension from the filepaths and capitalize the 1st letter of the file name
    filetopic= Path(filepath).stem
    name = filetopic.title()
    print(name)
    pdf.set_font(family="Times", style="B", size=18)  # set the font settings
    pdf.set_text_color(0,0,0)  # set the color settings
    pdf.cell(w=50, h=14 , align="L",txt=name,ln=1 , border=0)

    # get/read the data from each of the text files and store them in a variable using context text manager
    with open(filepath, "r") as file:
        content = file.read()
    pdf.set_font(family="Times", style="I", size=12)  # set the font settings
    pdf.set_text_color(0, 0, 0)  # set the color settings
    pdf.multi_cell(w=0,h=8,txt=content)

# generate pdf file (the pdf file should contain 4 pages , each file name as title on  a separate page)
pdf.output("PDF/animals.pdf")