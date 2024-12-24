import os
import subprocess

def create(name):
    global f
    global tex_name
    tex_name = name
    f = open("{file_name}.tex".format(file_name = name), 'a')

def clear():
    with open(f"{tex_name}.tex", "w") as k:
        pass 

def texcurl(string):
    return "{" + string + "}"

def preamble(type, title, author):
    f.write(fr"\documentclass" + texcurl(fr"{type}") + "\n")
    f.write(fr"\title" + texcurl(fr"{title}") + "\n")
    f.write(fr"\author" + texcurl(fr"{author}") + "\n")

def ong_bruh():
    f.write(fr"\begin{{document}}" + "\n")
    f.write(fr'\maketitle' + "\n")

def line(string, double):
    if double == False:
        f.write(string + "\n")
    elif double == True:
        f.write(string + "\\\\" + "\n")

def gahzamn():
    f.write(fr"\end{{document}}")

def compile():
    subprocess.run(["open", "-a", "TeXShop", f"{tex_name}.tex"])



