#include <iostream>
#include <fstream>
#include <string>
#include <vector>

const int LENGTH = 135;

int get_row_options(std::vector<std::string>& line_buffer, int line) {
	int total_options = 0;
	int rolls_adj = 0;

	const int line_len = line_buffer[1].length();

	for (int i = line-1; i < line+2; i++) {
		for (int j = 0; j < 2; j++) {
			if (line_buffer[i][j] == '@') {
				rolls_adj += 1;
			}
		}
	}
	if (line_buffer[line][0] == '@') {
		if (rolls_adj < 5) {
			total_options += 1;
			line_buffer[line][0] = '.';
		}
	}

	for (int j = 1; j < line_len - 1; j++) {
		for (int i = line-1; i < line+2; i++) {
			// add j+1, remove j-2
			if (line_buffer[i][j+1] == '@') {
				rolls_adj += 1;
			}
			if ((j > 1) && (line_buffer[i][j-2] == '@')) {
				rolls_adj -= 1;
			}
		}

		if ((line_buffer[line][j] == '@') && (rolls_adj < 5)) {
			total_options += 1;
			line_buffer[line][j] = '.';
		}
	}

	for (int i = line-1; i < line+2; i++) {
		if (line_buffer[i][line_len-3] == '@') {
			rolls_adj -= 1;
		}
	}

	if ((line_buffer[line][line_len-1] == '@') && (rolls_adj < 5)) {
		total_options += 1;
		line_buffer[line][line_len-1] = '.';
	}

	return total_options;
}

int get_options(std::vector<std::string>& line_buffer) {
	int total_options = 0;

	for (int i = 1; i < line_buffer.size()-1; i++) {
		total_options += get_row_options(line_buffer, i);
	}

	return total_options;
}

std::string get_padding() {
	std::string out_str;
	for (int i = 0; i < LENGTH; i++) {
		out_str += '.';
	}
	return out_str;
}

int main() {
	std::ifstream file("input");

	std::vector<std::string> line_buffer;
	std::string line;

	line_buffer.push_back(get_padding());

	int total_options = 0;

	while (std::getline(file, line)) {
		line_buffer.push_back(line);
	}

	line_buffer.push_back(get_padding());

	int n_iterations = 9;

	while (true) {
		int new_options = get_options(line_buffer);
		if (new_options == 0) break;
		total_options += new_options;
		n_iterations ++;
	}

	std::cout << "total options: " << total_options << std::endl;
	std::cout << "total iterations: " << n_iterations << std::endl;

	return 0;
}
