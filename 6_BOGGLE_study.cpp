#include <iostream>
#include <vector>
using namespace std;

const int dy[8] = {-1,-1,-1,0,0,1,1,1};
const int dx[8] = {-1,0,1,-1,1,-1,0,1};
int recursive_count = 0;


bool isInRange(int y, int x) {
	if((y >= 0 && y <= 4 ) && (x >= 0 && x<= 4)) {
		return true;
	} else {
		return false;
	}
}

bool recur(int y, int x, const string& word, vector< vector<char> >& board) {
	if(board[y][x] == word[0]) {
		if(word.size() == 1) {
			return true;
		}
		
		for(int i=0; i<8; i++){
			int nextY = y + dy[i];
			int nextX = x + dx[i];
			if (isInRange(nextY, nextX)){
				string word_sliced = word.substr(1);
				if(recur(nextY, nextX, word_sliced, board)){
					return true;
				}
			}
		}
		return false;

	} else {
		return false;
	}
}

int main() {
	int board_count;
	cin >> board_count;

	for(int i=0;i<board_count;i++){
				
		vector< vector<char> > board;
		for(int j=0;j<5;j++){
			string string_row;
			cin >> string_row;
			vector<char> row(string_row.begin(), string_row.end());
			board.push_back(row);
		}

		int word_count;
		cin >> word_count;
		vector<string> words;
		for(int j=0;j<word_count;j++){
			string word;
			cin >> word;
			words.push_back(word);
		}

		vector<string>::iterator iter = words.begin();
	
		for(vector<string>::iterator word_iter = words.begin(); word_iter != words.end(); ++word_iter) {
			string result = "NO";
			bool isFound = false;
			for(int j=0;j<5;j++) {
				for(int k=0;k<5;k++) {
					if(recur(j, k, *word_iter, board)){
						isFound = true;
						result = "YES";
						break;
					}
					if(isFound) break;
				}
				if(isFound) break;
			}
			cout << *word_iter << " " << result << "\n";
		}
	}
	
	return 0;
}

