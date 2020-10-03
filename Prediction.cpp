#include "Predictor.h"

Predictor::Predictor()
{}

void Predictor::store_data(int* price, int* square_feet, int size) {
	write_file.open("data_file.txt");

	for (int i = 0; i < size; i++) {
		write_file << square_feet[i] << " " << price[i] << endl;
	}

	write_file.close();
}
