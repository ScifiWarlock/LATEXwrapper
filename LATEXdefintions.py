import os
import subprocess
import datetime

date = datetime.date.today()
ss_date = date.strftime("%Y-%m-%d")

ss_dir = "/Users/omkar/Desktop/Screenshots/"

def create(name):
    global fl
    global tex_name
    tex_name = name
    fl = open("{file_name}.tex".format(file_name = name), 'a')

def clear():
    with open(f"{tex_name}.tex", "w") as k:
        pass 

def texcurl(string):
    return "{" + string + "}"

#initial header/setup
def preamble(type, title, author):
    fl.write(fr"\documentclass" + texcurl(fr"{type}") + "\n")
    fl.write(fr"\title" + texcurl(fr"{title}") + "\n")
    fl.write(fr"\author" + texcurl(fr"{author}") + "\n")
    fl.write(fr"\usepackage{{graphicx}}" + "\n")
    fl.write(fr"\graphicspath" + "{" + texcurl(fr"{ss_dir}") + "}" + "\n")
    fl.write("\n")

#ong_bruh lets begin
def ong_bruh():
    fl.write(fr"\begin{{document}}" + "\n")
    fl.write(fr'\maketitle' + "\n")


#line has function searching; similar to implicit concat
#no need for splitting up the string
def line(string, double):
    retstring = ""
    if ";" in string:
        split_list = string.split(";")
        for element in split_list:
            if "(" in element:
                retstring += str(eval(element))
            else:
                retstring += element
        if double == False:
            fl.write(retstring + "\n")
        elif double == True:
            fl.write(retstring + "\\\\" + "\n")
            fl.write("\n")
    else:
        if double == False:
            fl.write(string + "\n")
        elif double == True:
            fl.write(string + "\\\\" + "\n")

#math formatting (math italics)
def math(string):
    return "$" + string + "$"

#time must be in hh.mm and 12 hour time not 24
def image(time):
    for filename in os.listdir(ss_dir):
        if str(time) in filename:
            fl.write("\n")

            #format it so that it fits the text flow
            fl.write(fr"\begin{{figure}}[h]" + "\n")
            fl.write(fr"\includegraphics" + "[width=5cm, height=5cm]" + texcurl(fr"{filename}") + "\n")
            fl.write(fr"\end{{figure}}")

#end the script
def gahzamn():
    fl.write(fr"\end{{document}}")

#compile the python script and open it in Texshop file
def compile():
    subprocess.run(["open", "-a", "TeXShop", f"{tex_name}.tex"])



