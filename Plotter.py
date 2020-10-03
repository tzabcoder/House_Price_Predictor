import matplotlib.pyplot as plt

#The lists have corresponding points @ i
size_list = []
price_list = []

#Open the file and read the data into the lists
def openFile():
    file = open("C:\\Programming\\Cpp_Code\Machine_Learning\\HousePricePredictor_VS\\HousePricePrediction\HousePricePrediction\\data_file.txt", "r")
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
        size_list.append(size_num)
        price_list.append(price_num)
    
    file.close() #Close the file

#Convert the string to a integer
def convert_string(temp):
    num = (int)(temp)
    return num

def graph():
    plt.title("House Pricing Based on sqft")
    plt.xlabel("Size in sqft")
    plt.ylabel("Price in Hundred Thousands")
    plt.scatter(size_list, price_list)
    plt.show()

#Display the two lists
def display():
    print(size_list)
    print(price_list)

#main function
def main():
    openFile()
    graph()
    display()

#Calls the main function
if __name__ == "__main__":
    main()