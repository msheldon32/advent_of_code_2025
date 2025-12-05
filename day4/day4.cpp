#include <iostream>
#include <fstream>
#include <string>
#include <deque>

const int LENGTH = 135;

int get_options(std::deque<std::string>& line_buffer) {
	int total_options = 0;
	int rolls_adj = 0;

	const int line_len = line_buffer[1].length();

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 2; j++) {
			if (line_buffer[i][j] == '@') {
				rolls_adj += 1;
			}
		}
	}
	if (line_buffer[1][0] == '@') {
		if (rolls_adj < 5) {
			total_options += 1;
		}
	}

	for (int j = 1; j < line_len - 1; j++) {
		for (int i = 0; i < 3; i++) {
			// add j+1, remove j-2
			if (line_buffer[i][j+1] == '@') {
				rolls_adj += 1;
			}
			if ((j > 1) && (line_buffer[i][j-2] == '@')) {
				rolls_adj -= 1;
			}
		}

		if ((line_buffer[1][j] == '@') && (rolls_adj < 5)) {
			total_options += 1;
		}
	}

	for (int i = 0; i < 3; i++) {
		if (line_buffer[i][line_len-3] == '@') {
			rolls_adj -= 1;
		}
	}

	if ((line_buffer[1][line_len-1] == '@') && (rolls_adj < 5)) {
		total_options += 1;
	}

	return total_options;
}

int main() {
	std::ifstream file("input");

	std::deque<std::string> line_buffer;
	std::string line;

	line_buffer.push_back(std::string(".", LENGTH));

	int total_options = 0;

	while (std::getline(file, line)) {
		line_buffer.push_back(line);

		if (line_buffer.size() > 3) {
			line_buffer.pop_front();
		}

		if (line_buffer.size() == 3) {
			total_options += get_options(line_buffer);
		}
	}

	line_buffer.push_back(std::string(".", LENGTH));
	line_buffer.pop_front();

	total_options += get_options(line_buffer);

	std::cout << "total options: " << total_options << "\n";

	return 0;
}
