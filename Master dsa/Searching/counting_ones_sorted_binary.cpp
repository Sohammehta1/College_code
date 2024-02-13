#include<iostream>

int countingOnes(int arr[], int n){
        int count = 0;
        int mid, low = 0, high = n-1;
        
        while (low <= high)
        {
           mid = (low+high)/2;
           if(arr[mid] == 0)
                low = mid+1;
           else{
                if((mid-1)>=0 and arr[mid-1]==1)
                {
                    int idx = mid;
                    while(idx >=0 and arr[idx]==1)
                    {
                        count ++;
                        idx --;
                    }
                }
                count += (n-1-mid);
                break;
           }
        }
        return count;
        
}

int main(){
    int arr[] = {0,0,0,0};
    std :: cout << countingOnes(arr,4) << std :: endl;


    return 0; 
}