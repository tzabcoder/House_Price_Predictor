from Plotter import Plotter

priceArray = []
sizeArray = []
size = 0

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
    file = open("C:\\Programming\\Price_Predictor\\data_file.txt", "r")
    for data in file:        
        for x in range(len(data)):
            c = data[x]
            if c == ' ':
                size = data[0:x]
                price = data[x+1:len(data)-1]
        
        #Convert the strings to integers
        size_num = convert_string(size)
        price_num = convert_string(price)
        #insert the integer data into the lists
        sizeArray.append(size_num)
        priceArray.append(price_num)
    
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

def main():
    input_data()
    write_file()
    p = Plotter()
    p.openFile()
    p.graph()

    #calculate the cost function here
    #Then gradient descent algorithm
    #have user input the price
    #output estimated cost with margin of error
    #Replot the points??

    disp_data()

if __name__ == "__main__":
    main()