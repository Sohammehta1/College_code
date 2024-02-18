#include<iostream>

int inf_search(int arr[], int n, int target){
    if(arr[0]==target)
        return 0;
    int low = 1,high =1;
    while(target > arr[high]){
        low = high;
        high *= 2;
    }
    // now target is inbetween low and high and now we can apply standard binary search
    while(low<=high)
    {
        int mid = (low+high)/2;
        if(arr[mid] == target)
            return mid;
        if(arr[mid] < arr[high])
            high = mid-1;
        else
            low = mid+1;
    }
    return -1;
}

int main(){
    return 0;
}