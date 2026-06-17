#include <bits/stdc++.h>

using namespace std;

vector<int> slidingSubarrayBeauty(vector<int>& arr, int k, int x) {
    vector<int> result;
    vector<int> freq(101, 0); // values range -50..50, offset by +50

    for (int i = 0; i < (int)arr.size(); ++i) {
        freq[arr[i] + 50]++;

        if (i >= k - 1) {
            int count = 0;
            int beauty = 0;
            for (int v = 0; v < 50; ++v) { // only check negative values (-50..-1)
                count += freq[v];
                if (count >= x) {
                    beauty = v - 50;
                    break;
                }
            }
            result.push_back(beauty);

            int outIdx = i - k + 1;
            freq[arr[outIdx] + 50]--;
        }
    }

    return result;
}

int main() {
    string input;
    getline(cin, input);
    stringstream ss(input);
    vector<int> arr;
    int num;
    while (ss >> num) {
        arr.push_back(num);
    }

    int k, x;
    cin >> k >> x;

    vector<int> result = slidingSubarrayBeauty(arr, k, x);

    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << " ";
    }

    cout << endl;

    return 0;
}
