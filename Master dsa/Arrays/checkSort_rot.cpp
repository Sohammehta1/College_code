#include<iostream>

int main(){
    int arr[] ={16,1,2,3,5};
    int n = sizeof(arr)/4;
    int i = 0;
    while(i<n and arr[i]>arr[i+1])
        i++;
    int j = i;
    int next;
    do{
        next = (j+1)%n;
        if(arr[j]<arr[next])
            j = next;
        else
            break;
        
    }while(j!=i);
    if(j==i or (j+1)%n == i)
        std :: cout << "The array is sorted" << std :: endl;
    else
        std :: cout << "The array is not sorted" << std :: endl;
    return 0;
}