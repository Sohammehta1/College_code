#include<iostream>
#include<vector>

void max_con_flips(int arr[], int n){

    // NAIVE SOLUTIION : TC : O(2N); SC : O(N)
    // int i =0;
    // std :: vector<std :: pair<int,int>> max0,max1; // for keeping track of groups of ones and zeroes
    // while(i<n){
    //     if(arr[i]==1)
    //     {
    //         int e = i;
    //         while (arr[i]==1)
    //             i++;
            
    //         max1.push_back({e,i-1});
    //     }
    //     else{
    //         int e = i;
    //         while (arr[i]==0)
    //             i++;
            
    //         max0.push_back({e,i-1});
    //     }
    // }
    // if(max1.size()>max0.size())
    //     for(std :: pair p :  max0)
    //         std :: cout << p.first << " to " << p.second << std :: endl; 
    // else
    //     for(std :: pair p :  max1)
    //         std :: cout << p.first << " to " << p.second << std :: endl; 

    // A MORE TIME EFFICIENT SOLUTION

    //  find out the minimum group and then traverse array again to print the indices.
}

int main(){

    int arr[] ={1,1,0,0,0,1,0,0,1};
    int n = sizeof(arr)/sizeof(arr[0]);
    max_con_flips(arr,n);
    return 0;
}