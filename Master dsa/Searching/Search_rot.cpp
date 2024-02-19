#include<iostream>

    int search_rotated_arr(int arr[], int n, int target){
        // Instead of searching for minimum first (linear) and then using binary search,
        // we can directly using binary search and find the element.

       int low  =0, high = n-1;
       while(low<=high){
        int mid = (low+high)/2;
        if(arr[mid] == target)
            return mid;
        if(arr[mid]>=arr[low]){ // left partition is sorted
            if(target >=arr[low] and target < arr[mid])
                high = mid-1;
            else
                low = mid+1;
        }
        else{ // right partition may be  sorted
            if(target > arr[mid] and target <=arr[high])
                low = mid+1;
            else
                high = mid-1;
        }
       }
       return -1;
    }

int main(){
    return 0;
}