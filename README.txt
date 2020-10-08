House_Price_Predictor:

Files Includes With This Project: 
  Predictor.py
  Plotter.py
  data_file.txt

Overview: 
  This program takes input data entered by the user or reads data from an existing file called "data_file.txt". Once the data is read in, the Matplotlib library plots a scatter plot and draws a linear regression line to best fit the data. Once the line is drawn, the program prompts the user to enter a house's square footage. Then will predict the price based on that square footage. The program outputs the predicted value with a +-5% margin of error. Then adds the correct price back into the dataset for more precision. 
  
Limitations & Decisions:
  The program predicts a price based on square footage alone and does NOT take into account lot size, or any other features of the land. I decided to use Python for runntime, and ease of programmign

File Sizes:
  Predictor.py - 5KB
  Plotter.py - 2KB

total - 7KB

File Structure
C:
  Price_Predictor
    Predictor.py
    Plotter.py
    data_file.txt
    
written by Trevor Zabilowicz completed: 10/7/2020
