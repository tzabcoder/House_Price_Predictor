#include <iostream>
#include <sstream>
#include "Prediction.h"
using namespace std;

bool check_number(string);
int convert_to_int(string);
void enter_data(int*, int*, int);

//Main driver of the program
int main() {
	
	//Creates a new instance of the Prediction class
	Prediction p;
	
	bool enter_status = true;
	int size = 0;
	string test_input;
	
	//Array declarations
	int *priceArray;
	int *sizeArray;
	
	while(enter_status){
		cout<<"Enter the number of data pieces: ";
		cin>>test_input;
		
		if(check_number(test_input)){
			size = convert_to_int(test_input);
			enter_status = false;
		} else {
			cout<<"Input is not a number..."<<endl;
			enter_status = true;
		}	
	}
	
	//Array Initializations
	priceArray = new int[size];
	sizeArray = new int[size];
	
	enter_data(priceArray, sizeArray, size);
	//calculate the data here
	//Price Array has all of the price variables (y)
	//Size Array has all of the size variables (x)
	//The data pieces are paired at point i
	
	//Prompt the user for a predicted house price
	
	//Display the data of the predicted house price
	
	delete[] priceArray;
	delete[] sizeArray;
	return 0;
}

//Check if the user input was a number
bool check_number(string temp){
	
	for(int i = 0; i < temp.length(); i++){
		if(isdigit(temp[i]) == false)
			return false;
	}
	return true;
}

//Converts string to a number
int convert_to_int(string input){
	int number;
	
	stringstream ss;
	ss << input;
	ss >> number;
	
	return number;
}

//enter the data into the arrays
void enter_data(int* price, int* squareFeet, int size){
	bool validate;
	string temp_size_input;
	string temp_price_input;
	
	for(int i = 0; i < size; i++){
		system("CLS");
		validate = true;
		
		while(validate){	
			cout<<"Use only NUMBERS for the size and the price of the data..."<<endl;
			cout<<"Enter the size of "<<i<<" training variable (is square feet): ";
			cin>>temp_size_input;
			cout<<"Enter the price of "<<i<<" training variable (in thousands): $";
			cin>>temp_price_input;
			
			if(check_number(temp_size_input) == true){
				squareFeet[i] = convert_to_int(temp_size_input);
				validate = false;
			} else { 
				cout<<"Size input was not a number..."<<endl;
				validate = true;
			}
			if(check_number(temp_price_input) == true){
				price[i] = convert_to_int(temp_price_input);
			} else {
				cout<<"Price input was not a number..."<<endl;
				validate = true;
			}
		}
	}	
	
}







