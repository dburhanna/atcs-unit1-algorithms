#include <iostream>
#include <set>

using namespace std;

int main() {
    set<int> values = {50, 25, 75, 10, 35};

    for (int value : values) {
        cout << value << " ";
    }

    cout << endl;
    cout << (values.find(35) != values.end());

    return 0;
}
