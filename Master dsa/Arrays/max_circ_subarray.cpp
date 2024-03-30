#include<iostream>
#include<climits>

#include"kadanes_algo.cpp"



void max_circular_subarray(int arr[], int n){
    // int result = INT_MIN;
    // for(int i =0;i<n;i++){
    //         int max_so_far= 0;
    //         int max_loop = arr[(i+1)%n];
    //         int sum = 0;
    //         int j = (i+1)%n;
    //    do{
    //         sum = std :: max(sum+arr[j],arr[j]);
    //         max_loop = std :: max(max_loop,sum);
    //         j = (j+1)%n;
    //     }while(j!= (i+1)%n);
    //     result = std :: max(max_loop,result);
    // }
    // std :: cout << "Max sum is : " << result << std :: endl;

     // Efficient approach 
        int ksum = maxSubarraySum(arr,n);
        if(ksum < 0){
             std :: cout <<  ksum << std :: endl; // if ksum < 0, that means all elements are negative and maxsum will be ksum which will be the least negative element
             return;
        }
        int inverted[n];
        int total = 0;
        for(int i = 0;i<n;i++){
            inverted[i] = -arr[i];
            total += arr[i];
        }
        
        int isum = maxSubarraySum(inverted,n);
        
        int result = max(ksum, isum+total);
        std :: cout  << result << std :: endl;

}

int main(){
    int arr[] = {11,-12,3,-1,5};
    max_circular_subarray(arr,5);
    
    return 0;
}