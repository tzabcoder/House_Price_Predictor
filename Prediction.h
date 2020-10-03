#ifndef PREDICTION_H
#define PREDICTION_H
#include <iostream>
#include <fstream>
using namespace std;

class Predictor
{
public:
	//Constructor
	Predictor();
	void cost_function();
	void graph_function();
	void store_data(int*, int*, int);
private:
	ofstream write_file;
};

#endif
