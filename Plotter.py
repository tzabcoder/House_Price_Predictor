import matplotlib.pyplot as plt

#The lists have corresponding points @ i
size_list = []
price_list = []

class Plotter:
    #The lists have corresponding points @ i
    size_list = []
    price_list = []

    #Open the file and read the data into the lists
    def openFile(self):
        file = open("C:\\Programming\\Price_Predictor\\data_file.txt", "r")
        for data in file:        
            for x in range(len(data)):
                c = data[x]
                if c == ' ':
                    size = data[0:x]
                    price = data[x+1:len(data)-1]
            
            #Convert the strings to integers
            size_num = int(size)
            price_num = int(price)
            #insert the integer data into the lists
            size_list.append(size_num)
            price_list.append(price_num)
        
        file.close() #Close the file

    def graph(self):
        plt.title("House Pricing Based on sqft")
        plt.xlabel("Size in sqft")
        plt.ylabel("Price in Hundred Thousands")
        plt.scatter(size_list, price_list)
        plt.show()