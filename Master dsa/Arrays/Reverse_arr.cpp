#include<iostream>
using namespace std;


    void reverse_arr(int arr[], int n){
    //int n = sizeof(arr)/sizeof(arr[0]); This does not work since sizeof function returns size of pointer when the array is passed to the function
    int a;
    for(int i =0;i<n/2;i++){
        a = arr[n-i-1];
        arr[n-i-1] = arr[i];
        arr[i] = a;
    }
}



int main(){
    int arr1[] = {1,2,3,4};
    int n = sizeof(arr1)/sizeof(arr1[0]);
    reverse_arr(arr1,n);
    for(int i : arr1)
        cout << i << " ";
    cout << endl;
    return 0;
}