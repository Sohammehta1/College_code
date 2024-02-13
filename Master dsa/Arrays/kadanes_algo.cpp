#include<iostream>
using namespace std;

int maxSubarraySum(int arr[], int n) {
    int max_sum = arr[0];  // Initialize the maximum sum with the first element
    int current_sum = arr[0];  // Initialize the current sum with the first element

    for (int i = 1; i < n; ++i) {
        // Update the current sum to include the current element or start a new subarray
        current_sum = max((arr[i]), current_sum + arr[i]);

        // Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum);
    }

    return max_sum;
}