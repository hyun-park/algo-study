#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {
	int test_case;
	cin >> test_case;

	for(int i=0;i<test_case;i++){
		int student;
		cin >> student;
		int group;
		cin >> group;
		vector< set<int> > friends_group;
		vector< bool > isGrouped(student, false);

		for(int j=0;j<group;j++){
			int first;
			int second;
			set<int> friends;
			cin >> first;
			friends.insert(first);
			cin >> second;
			friends.insert(second);
			friends_group.push_back(friends);
		}

		for(int j=0;j<student-1;j++){
			if(!isGrouped[j]){
				for(int k=j+1;k<student;k++){
					if(!isGrouped[k]){
						
					}
				}
			}
		}
	}
	return 0;
}
