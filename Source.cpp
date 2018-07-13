#include <iostream>
#include <fstream>

//python script must be located in the same directory as the c++ code that calls the script

int main()
{
	/// CODE HERE IS FOR LINKING PYTHON AND C++ 
	/// DO NOT EDIT
	/// -------------------------------------------
	system("chcp 65001");
	system("CLS");
	std::cout << "Running Script..." << std::endl;
	system("python scraper.py");
	/// -------------------------------------------


	return 0;
}
