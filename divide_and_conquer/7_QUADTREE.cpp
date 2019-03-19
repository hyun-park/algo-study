#include <iostream>
#include <string>
using namespace std;


string recur(string::iterator& it){
	char head = *it;
	++it;
	
	// base case
	if(head == 'b' || head == 'w')
		return string(1, head);

	// job code
	string upperLeft = recur(it);
	string upperRight = recur(it);
	string lowerLeft = recur(it);
	string lowerRight = recur(it);

	return "x" + lowerLeft + lowerRight + upperLeft + upperRight;	
}

int main() {

	string compressed;
	cin >> compressed;
	string::iterator compressed_it = compressed.begin();
	cout << recur(compressed_it) << "\n";
	return 0;
}

