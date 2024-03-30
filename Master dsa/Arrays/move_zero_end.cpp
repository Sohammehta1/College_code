#include<iostream>
#include<time.h>
#include <iomanip>


void zeroes_to_end(int arr[], int n){
    int zero_idx=0;
    for(int i =0;i<n;i++){
        
        if(arr[i] ==0)
        {
            zero_idx =i;
            while (zero_idx< n and  arr[zero_idx] ==0)
               zero_idx++;
            if(zero_idx < n){
                arr[i] = arr[zero_idx];
                arr[zero_idx] = 0;

            }
            else 
                return;
            
            
        }
    }

    // Best solution
    // for (int  i = 0; i < n; i++)
    // {
    //     if(arr[i]!=0){
    //         std :: swap(arr[i],arr[zero_idx]);
    //         zero_idx ++;
    //     }
    // }
    
    return;
}

int main(){
    int arr[] = {1,2,0,0,0,3,5,6,0};
    
    time_t start,end;

    time(&start);
    std :: ios_base::sync_with_stdio(false); 
    zeroes_to_end(arr,9);
    time(&end); 
    double time_taken = double(end-start);
    std :: cout << "Time required : " << time_taken <<std :: setprecision(5) <<std :: endl;
    return 0;
}