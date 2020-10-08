import matplotlib.pyplot as plt
import numpy as np

#The lists have corresponding points @ i
size_list = []
price_list = []

class Plotter:
    #The lists have corresponding points @ i
    size_list = []
    price_list = []
    line_slope = 0
    yintercept = 0

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

    def draw_line(self):
        slope, intercept = np.polyfit(size_list, price_list, 1)
        self.line_slope = slope
        self.yintercept = intercept
        abline_values = [slope * i + intercept for i in size_list]
        plt.scatter(size_list, price_list)
        plt.plot(size_list, abline_values, 'b')
        plt.title("Best Fit Line")
        plt.show()
        
    def graph(self):
        plt.title("House Pricing Based on sqft")
        plt.xlabel("Size in sqft")
        plt.ylabel("Price in Hundred Thousands")
        plt.scatter(size_list, price_list)
        plt.show()

    def predict_cost(self, size):
        #create upper and lower bound
        finalPrice = (size)*(self.line_slope) + self.yintercept
        temp = finalPrice * 0.05
        upperBound = finalPrice + temp
        lowerBound = finalPrice - temp
        print("The predicted value: $", round(finalPrice, 2))
        print("The upper bound price is: $", round(upperBound,2))
        print("The lower bound price is: $", round(lowerBound,2))
