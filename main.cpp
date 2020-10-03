#include <iostream>
#include <sstream>
#include <fstream>
#include "Predictor.h"
using namespace std;

int get_size();
void read_data(int*, int*);
bool check_number(string);
int convert_to_int(string);
void enter_data(int*, int*, int);

//Main driver of the program
int main() {

	//Creates a new instance of the Prediction class
	Predictor p;

	bool skip;
	bool enter_status = true;
	bool can_read = true;
	int size = 0;
	string test_input, confirm_read;

	//Array declarations
	int* priceArray;
	int* sizeArray;

	while(can_read) {
		cout << "Read data from the file?: ";
		getline(cin, confirm_read);

		if (confirm_read == "yes" || confirm_read == "Yes") { //Read data from the file
			int numofdata = get_size();

			priceArray = new int[numofdata];
			sizeArray = new int[numofdata];

			read_data(priceArray, sizeArray);
			can_read = false;
			skip = false;
			
			p.store_data(priceArray, sizeArray, numofdata); //Stores the data in a file
		}
		else if (confirm_read == "no" || confirm_read == " No") {
			can_read = false;
			skip = true;
		}
		else {
			cout << "Invalid Input..." << endl;
			system("pause");
		}
		system("CLS");
	}

	//If the user wishes to enter data into the file
	if (skip) {
		while (enter_status) {
			cout << "Enter the number of data pieces: ";
			cin >> test_input;

			if (check_number(test_input)) {
				size = convert_to_int(test_input);
				enter_status = false;
			}
			else {
				cout << "Input is not a number..." << endl;
				enter_status = true;
			}
		}

		//Array Initializations
		priceArray = new int[size];
		sizeArray = new int[size];

		enter_data(priceArray, sizeArray, size);
		p.store_data(priceArray, sizeArray, size); //Stores the data in a file
	}

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

int get_size() {
	int m = 0;
	string temp;
	ifstream file;

	file.open("data_file.txt");
	while (!file.eof()) {
		getline(file, temp);
		m++;
	}
	file.close();
	
	m = m-1;

	return m;
}

void read_data(int* priceArray, int* sizeArray) {
	ifstream file;
	string data;
	int size_int, price_int, counter = 0;
	string size_temp, price_temp;

	file.open("data_file.txt");
	while (!file.eof()) {
		getline(file, data);
		int pos = data.find(' ');

		size_temp = data.substr(0, pos);
		price_temp = data.substr(pos + 1, data.length());

		size_int = convert_to_int(size_temp);
		price_int = convert_to_int(price_temp);

		sizeArray[counter] = size_int;
		priceArray[counter] = price_int;
		counter++;
	}
	file.close();
}

//Check if the user input was a number
bool check_number(string temp) {

	for (int i = 0; i < temp.length(); i++) {
		if (isdigit(temp[i]) == false)
			return false;
	}
	return true;
}

//Converts string to a number
int convert_to_int(string input) {
	int number;

	stringstream ss;
	ss << input;
	ss >> number;

	return number;
}

//enter the data into the arrays
void enter_data(int* price, int* squareFeet, int size) {
	bool validate;
	string temp_size_input;
	string temp_price_input;

	for (int i = 0; i < size; i++) {
		system("CLS");
		validate = true;

		while (validate) {
			cout << "Use only NUMBERS for the size and the price of the data..." << endl;
			cout << "Enter the size of " << i + 1 << " training variable (is square feet): ";
			cin >> temp_size_input;
			cout << "Enter the price of " << i + 1 << " training variable (in thousands): $";
			cin >> temp_price_input;

			if (check_number(temp_size_input) == true) {
				squareFeet[i] = convert_to_int(temp_size_input);
				validate = false;
			}
			else {
				cout << "Size input was not a number..." << endl;
				validate = true;
			}
			if (check_number(temp_price_input) == true) {
				price[i] = convert_to_int(temp_price_input);
			}
			else {
				cout << "Price input was not a number..." << endl;
				validate = true;
			}
		}
	}
}







