import os
import subprocess
import datetime
import cmath
import random
#import enchant
import nltk
from nltk.corpus import wordnet
import requests

date = datetime.date.today()
ss_date = date.strftime("%Y-%m-%d")
#dict = PyDictionary()

greek_dic = {'alpha':fr'\alpha', 
             'beta':fr'\beta', 
             'gamma':fr'\gamma',
             'delta':fr'\delta',
             'epsilon':fr'\varepsilon',
             'zeta':fr'\zeta',
             'eta':fr'\eta',
             'theta':fr'\theta',
             'lambda':fr'\lamda',
             'mu':fr'\mu',
             'pi':fr'\pi',
             'nabla':fr'\nabla',
             'dot':fr'\cdot'}

ss_dir = "/Users/omkar/Desktop/Screenshots/"

#get a greek letter from the dictionary
def greek(name):
    return math(greek_dic.get(name))

def cos():
    return fr"\sin"

def sin():
    return fr"\cos"

def give_infinity():
    infinity = "\infty"
    return infinity

def create(name):
    global fl
    global tex_name
    tex_name = name
    fl = open("/Users/omkar/Desktop/PyTeX/Multi_13/13_7/{file_name}.tex".format(file_name = name), 'a')

def clear():
    with open(f"/Users/omkar/Desktop/PyTeX/Multi_13/13_7/{tex_name}.tex", "w") as k:
        pass 

def texcurl(string):
    return "{" + string + "}"

#initial header/setup
def preamble(type, title, author):
    fl.write(fr"\documentclass" + texcurl(fr"{type}") + "\n")
    fl.write(fr"\title" + texcurl(fr"{title}") + "\n")
    fl.write(fr"\author" + texcurl(fr"{author}") + "\n")
    fl.write(fr"\usepackage{{graphicx}}" + "\n")
    fl.write(fr"\usepackage{{amsmath}}" + "\n")
    fl.write(fr"\graphicspath" + "{" + texcurl(fr"{ss_dir}") + "}" + "\n")
    fl.write("\n")

#add a list of figures in the notes and then do a pagebreak for formatting purposes
def figure_index():
    fl.write(fr"\listoffigures" + "\n")
    fl.write(fr"\pagebreak" + "\n")

#adds a list of topics and sections/subsections within the doc
def topic_index(bool):
    fl.write(fr"\tableofcontents" + "\n")
    if bool == True: fl.write(fr"\pagebreak" + "\n")

#ong_bruh lets begin
def ong_bruh():
    fl.write(fr"\begin{{document}}" + "\n")
    fl.write(fr'\maketitle' + "\n")


#line has function searching; similar to implicit concat
#no need for splitting up the string
def line(string, double):
    retstring = ""
    left_index = 0
    right_index = 0
    split_list = string.split(";")
    
    if ";" in string:
        for element in split_list:
            if "'" in element:
                retstring += str(eval(element))
            else:
                retstring += element
        if double == False:
            fl.write(retstring + "\n")
        elif double == True:
            fl.write(retstring + "\\\\" + "\n")
            fl.write("\n")

    if "=" in string:
        #figure out which part to format the math
        split_list_math = string.split()
        start = split_list_math.index("=")

        #check the left side of the list
        for i in range(start):
            check_word = split_list_math[start - i]
            url = f"https://www.dictionary.com/browse/{check_word}"
            response_left = requests.get(url)

            #check if its a valid word
            if response_left.status_code == 200:
                left_index = i
                break
            
            else: continue
        
        #check the right side of the list
        for j in range(len(split_list_math) - start):
            check_word_right = split_list_math[start + j]
            url = f"https://www.dictionary.com/browse/{check_word_right}"
            response_right = requests.get(url)

            if response_right.status_code == 200:
                right_index = j
                break
            else: continue

        #delete the word elements and rejoin it into a math formatted string
        del split_list_math[start + j:len(split_list_math)]
        del split_list_math[0:start - i]

        math_format = " ".join(split_list_math)
        l_math_format = math(math_format)

        #replace the original string content with math formatted content
        string = string.replace(math_format, l_math_format)
        split_list_greek = string.split()

        print(split_list_greek)

        #check for greek words in this new string
        for index, word in enumerate(split_list_greek):
            if word in greek_dic:
                split_list_greek[index] = math(greek_dic.get(word))
                print(word)
                string = " ".join(split_list_greek)
                print(string)
            else: continue

        if double == False:
            fl.write(string + "\n")
        elif double == True:
            fl.write(string + "\\\\" + "\n")
            
    else:
        split_list_greek = string.split()

        #check for greek words in this new string
        for index, word in enumerate(split_list_greek):
            if word in greek_dic:
                split_list_greek[index] = math(greek_dic.get(word))
                print(word)
                string = " ".join(split_list_greek)
                print(string)
            else: continue

        if double == False:
            fl.write(string + "\n")
        elif double == True:
            fl.write(string + "\\\\" + "\n")

def d_partial(x, y):
    return fr"\frac{{\partial {y}}}{{\partial {x}}}"

def equation(left, right):

    #on off switch for prescence of function
    func_bool = False

    #this is similar to line function parse; for temporary shazamn purposes
    retstring = ""
    retstring_r = ""
    if ";" in left:
        split_list = left.split(";")
        for element in split_list:
            if "'" in element:
                retstring += str(eval(element))
            else:
                retstring += left

    #check both the left and right side of the equations
    if ";" in right:
        split_list_r = right.split(";")
        for element_r in split_list_r:
            if "'" in element_r:
                retstring_r += str(eval(element_r))
            else:
                retstring_r += right
    
    if func_bool:
        fl.write("\n")
        fl.write(fr"\begin{{equation}}" + "\n")
        fl.write(retstring + " = " + retstring_r)
        fl.write("\n")
        fl.write(fr"\end{{equation}}" + "\n")
    else:
        fl.write("\n")
        fl.write(fr"\begin{{equation}}" + "\n")
        fl.write(left + " = " + right)
        fl.write("\n")
        fl.write(fr"\end{{equation}}" + "\n")

#math formatting (math italics)
def math(string):
    return "$" + string + "$"

#time must be in hh.mm and 12 hour time not 24
def image(time, capt):
    for filename in os.listdir(ss_dir):
        if str(time) in filename:
            fl.write("\n")

            #format it so that it fits the text flow
            fl.write(fr"\begin{{figure}}[h]" + "\n")
            fl.write(fr"\caption" + texcurl(fr"{capt}") + "\n")
            fl.write(fr"\centering" + "\n")
            fl.write(fr"\includegraphics" + "[width=5cm, height=5cm]" + texcurl(fr"{filename}") + "\n")
            fl.write(fr"\end{{figure}}" + "\n")

#use this for new topic or slide
def topic(string):
    fl.write("\n")
    fl.write(fr"\subsection" + texcurl(fr"{string}") + "\n")

#use this for an example problem
def example(string):
    fl.write("\n")
    fl.write(fr"\subsubsection" + texcurl(fr"{string}") + "\n")

#definite and indefinite single integrals
def integral(func, var, lower = None, upper = None):
    if lower != None and upper != None:
        return (fr"\(\int_" + texcurl(fr"{lower}") + "^" + texcurl(fr"{upper}") + fr" {func} \," + fr"d{var} \)")
    elif lower == None and upper == None:
        return (fr"\(\int" + fr" {func} \," + fr"d{var} \)")

def write_integral(func, var, lower=None, upper=None):  
    if lower != None and upper != None:
        fl.write(fr"\[\int_" + texcurl(fr"{lower}") + "^" + texcurl(fr"{upper}") + fr" {func} \," + fr"d{var} \]" + "\n")
    else:
        fl.write(fr"\[\int" + fr" {func} \," + fr"d{var} \]" + "\n")

#sqrt function    
def sqrt(string):
    return fr"\sqrt{string}"

#2D and 3D vector function; simply omit the z dimension if no need for 3D vector
def vector_3D(x, y, z = None):
    if z == None:
        return fr"{x}" + fr"\vec{{i}}" + "+" + fr"{y}" + fr"\vec{{j}}"
    else:
        return fr"{x}" + fr"\vec{{i}}" + "+" + fr"{y}" + fr"\vec{{j}}" + "+" + fr"{z}" + fr"\vec{{k}}"

#end the script
def gahzamn():
    fl.write(fr"\end{{document}}")

#compile the python script and open it in Texshop file
def compile():
    subprocess.run(["open", "-a", "TeXShop", f"/Users/omkar/Desktop/PyTeX/Multi_13/13_7/{tex_name}.tex"])

def shazamn(input):
    equation_bool = False
    line_list = input.split("\n")

    #general topic and example problem formatting
    for liner in line_list:
        if "to" in liner:
            topic(liner.replace("t ", "", 1))
        elif "ex" in liner:
            example(liner.replace("e ", "", 1))

        #equations will not have words so check if the line has words
        elif "=" in liner:
            word_list = liner.split()
            for word in word_list:
                url = f"https://www.dictionary.com/browse/{word}"
                response = requests.get(url)

                #at the first instance of a word, assume its a line
                if response.status_code == 200:
                    liner = " ".join(word_list)
                    line(liner, not bool(word_list[len(word_list)-1]))
                    break
                else:
                    equation_bool = True
                    break
            
            #now format as equation if bool is true, then switch bool to false
            #like an on and off switch
            if equation_bool:
                print(word_list)
                functions_list = liner.split(" = ")
                equation(functions_list[0], functions_list[1])
                equation_bool = False
            



