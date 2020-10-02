#!/usr/bin/env python3

import os

# import all the neccessary modules
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# function to generate pdf file arguments: filename(path to be saved)
# additional _info as body of the pdf
def generate(filename, additional_info):
    # initialize the sample style sheet
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    
    # create body of the pdf by specifying syles as BodyText
    report_info = Paragraph(additional_info, styles["BodyText"])
    # empty line
    empty_line = Spacer(1,20)

    # build the report by given arguments in the order,  first add empty_line
    # then report info and finally empty_line
    report.build([empty_line, report_info, empty_line])

# to read the contents of the .txt files list all the files in directory
dir_list = os.listdir("./supplier-data/descriptions/")

# initialize string variable to 
full_text = ""
for dirs in dir_list:
    # read all the .txt files in descriptions directory 
    with open("./supplier-data/descriptions/" + dirs) as f:
        # store whole file in a variable (as this is small file, no need 
        # to worry about memory consumption)
        reader = f.readlines()
        # In pdf we can't use \n for newline add <br/> for newline in
        # in between contents 
        full_text += "<br/>" + "name: " + reader[0].strip() + "<br/>" + "weight: " + reader[1].strip() + "<br/>"
    f.close()

generate("processed.pdf", full_text)