#include<iostream>

void binarySearch(int arr[], int n, int target, int &resultIdx){
    resultIdx = -1;
    int l = 0;
    int r = n-1;
    int mid;
    while(l<=r){
        mid = (l+r)/2;
        if(arr[mid] == target){
            resultIdx = mid;
            return;
        }
        else if(arr[mid]>target)
            r = mid-1;
        else
            l = mid+1;
    }
    
}

int binarySearch(int arr[], int n, int low, int high, int target){
    if(low<=high){
         int mid = (low+high)/2;
         int res;
        if(arr[mid] == target)
            return mid;
        if(arr[mid]>target)
            res =binarySearch(arr,n,low,mid-1,target);
        else if(arr[mid]<target)
            res = binarySearch(arr,n,mid+1,high,target);
        return res;
    }
    return -1;
   
}

int main(){

    int arr[]={1,2,3,4,5};
    int resultidx;
    //binarySearch(arr,5,2,resultidx);
    int result = binarySearch(arr,5,0,4,2);
    if(result != -1)
        std :: cout << "Target found at index : "<< result << std :: endl;
    else 
        std :: cout << "Target not found" << std :: endl;

    return 0;
}