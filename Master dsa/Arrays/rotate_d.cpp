#include<iostream>

void rotate_arr_d_inplace(int arr[],int n, int d){
    int replace,prev;
    while(d--)
    {
        prev = arr[0];
        for(int i =1;i<n; i++){
            replace = arr[i];
            arr[i] = prev;
            prev = replace;
        }
        arr[0] = replace;
    }
}

void rotate_arr_d(int arr[],int rot_arr[],int n, int d){
    if(d>=n)
        d %= n;
    if(d>0){
        int rot_idx=0;
        for(int i =d-1;i<n;i++)
        {
            rot_arr[rot_idx] = arr[i];
            std :: cout << i << " " << arr[i] << std  :: endl;
            rot_idx++;
        }
        for(int i =0;i<d-1;i++){
            rot_arr[rot_idx++] = arr[i];
        }
    }
    else
        return;
    
}

int main(){
    int arr[] = {10,15,20,35,40};
    int n = sizeof(arr)/sizeof(arr[0]);
    int rot_arr[n]; 
    rotate_arr_d_inplace(arr,n,4);
    rotate_arr_d(arr,rot_arr,n,4);
    for(int i = 0;i<n; i++)
        std :: cout << rot_arr[i]<<" ";
    std :: cout<< std :: endl;

    for(int i =0;i<n;i++)
        std :: cout << arr[i] << " ";
    
    return 0;
}