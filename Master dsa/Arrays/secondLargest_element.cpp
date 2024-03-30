#include<iostream>
#include<climits>

int main(){
    int arr[] ={1,2,3,15,5};
    int max_ = INT_MIN;
    int second_max = INT_MIN;
    for(int i: arr){
        if(i>max_)
        {
            second_max =max_;
            max_ = i;
        }
        else if(i>second_max){
            second_max = i;
        }
    }
    std :: cout << "Second max is : " << second_max << std :: endl;
    return 0;
}