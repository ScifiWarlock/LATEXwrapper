#Welcome to lattice scripting, a pseudo ml model that uses elliptic function lattices
import cmath

def read(input, epochs):
    #read each separate line
    line_list = input.split("\n")
    
    #make sure blank spaces are removed
    for index, liner in enumerate(line_list):
        line_list[index] = liner.strip()

    #cycle through the specified number of epochs
    for i in range(epochs):
        for liner in line_list:
            words = liner.split()

            existing_word_list = []

            with open("/Users/omkar/Desktop/PyTeX/pytex_lib/complex_numbers.txt", "r") as f:
                data = f.read()
                row_list = data.splitlines()
                print(row_list)

            #now check if the word is in the list
            for word in words:
                if word in row_list:
                    continue
                else:
                    with open("/Users/omkar/Desktop/PyTeX/pytex_lib/complex_numbers.txt", "r+") as f:
                        f.write(fr"{word}" + "\n,")
                    
