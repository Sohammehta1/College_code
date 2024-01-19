#include<iostream>

int check_dup_in_sorted(int arr[], int n){
    int dup_ele_idx=0;
    for(int i =1;i<n; i++){
        if(arr[i-1] == arr[i]){
            dup_ele_idx = i-1; 
            arr[i]= -1;
        }
        else if(arr[i-1] == -1 and arr[i]==arr[dup_ele_idx])
            arr[i] = -1;
        else
            dup_ele_idx = i;
    }
    int new_size = 1;
    for(int i =1;i<n;i++){
       if(arr[i] == -1 and arr[i-1] != -1){
            dup_ele_idx = i;
            while(dup_ele_idx < n and arr[dup_ele_idx] == -1 )
                dup_ele_idx ++;
            if(dup_ele_idx < n){
                arr[i] = arr[dup_ele_idx];
                arr[dup_ele_idx] = -1;
                new_size++;
            } 
            else
                break;
        }
        else if(arr[i] !=-1)
            new_size++;
           
    }
      for(int i =0;i<n;i++)
            std :: cout << arr[i] << " ";
        
    std :: cout << std :: endl;
    return new_size;
        
}

int main(){
    
    int arr[] = {10,20,20,30,30,30,30,40};
    int new_size = check_dup_in_sorted(arr,8);
    std :: cout << "New size is  : " << new_size << std :: endl;
    return 0;
}