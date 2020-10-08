from Plotter import Plotter
import numpy as np

priceArray = []
sizeArray = []
cost_values = []
hyp = 0.5
size = 0
cost_val = 0

def input_data():
    repeat = True
    while repeat:
        read_data = input("Read data from a file?: ")
        if(read_data == "yes" or read_data == "Yes"):
            get_file()
            repeat = False
        elif(read_data == "no" or read_data == "No"):
            read_input()
            repeat = False
        else: 
            print("Invalid input...")
            repeat = True

def get_file():
    size = 0
    file = open("C:\\Programming\\Price_Predictor\\data_file.txt", "r")
    for data in file:        
        for x in range(len(data)):
            c = data[x]
            if c == ' ':
                sizeH = data[0:x]
                price = data[x+1:len(data)-1]
        
        #Convert the strings to integers
        size_num = convert_string(sizeH)
        price_num = convert_string(price)
        #insert the integer data into the lists
        sizeArray.append(size_num)
        priceArray.append(price_num)
        size += 1
    
    file.close() #Close the file

#Convert the string to a integer
def convert_string(temp):
    num = (int)(temp)
    return num

#checks if the input is a number
def check_num(temp):
        try:
            val = int(temp)
            return False
        except ValueError:
            return True

def read_input():
    print("_____Input_____")
    isnum = True
    while isnum:
        size = input("Enter the number of houses: ")
        isnum = check_num(size)
        if (isnum == True):
                print("Invalid Input...")
        else:
            size = convert_string(size)

    for x in range(size):
        validateS = True
        while validateS:
            sizeTemp = input("Enter the size of the house in sqft: ")
            priceTemp = input("Enter the price of the house: ")

            validateS = check_num(sizeTemp)
            validateP = check_num(priceTemp)
            if(validateS == True or validateP == True):
                print("Invalid input...")
            else:
                sizeInt = convert_string(sizeTemp)
                priceInt = convert_string(priceTemp)
                sizeArray.append(sizeInt)
                priceArray.append(priceInt)

#Write the inout data to the file
def write_file():
    x = 0
    file = open("C:\\Programming\\Price_Predictor\\data_file.txt", "w")
    for listitem in sizeArray:
        file.write(str(listitem))
        file.write(" ")
        file.write(str(priceArray[x]))
        file.write('\n')
        x += 1

    file.close() #Close the file

def disp_data():
    print(sizeArray)
    print(priceArray)

def get_price():
    validate = True
    while(validate):
        temp = input("Enter the size of the house in sqft: ")
        validate = check_num(temp)

        if(validate == False):
            ret_val = convert_string(temp)
            return ret_val
        else:
            print("Invalid Input...")

def write_actual_val(val,size):
    file = open("C:\\Programming\\Price_Predictor\\data_file.txt", "a")
    file.write(str(size))
    file.write(" ")
    file.write(str(val))
    file.write('\n')
    file.close()

def main():
    cont = True
    callFunc = True
    input_data()
    write_file()

    while cont:
        p = Plotter()
        p.openFile()
        p.graph()
        p.draw_line()

        if(callFunc == True):
            input_size = get_price()
            p.predict_cost(input_size)
            actual_val = input("What was the actual value of the house?: ")
            actual_val = (float)(actual_val)
            write_actual_val(int(actual_val),int(input_size))

        confirm = input("Enter Another value?: ")
        if(confirm == "Yes" or confirm == "yes"):
            cont = True
            callFunc = True
        elif(confirm == "no" or confirm == "No"):
            cont = False
            callFunc = False
        else:
            cont = True
            callFunc = False
            print("Invalid Input...")

if __name__ == "__main__":
    main()