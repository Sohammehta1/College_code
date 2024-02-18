#include<iostream>
#include<cmath>

int sqroot(int num){
    int low = 1, high = num;
    int mid,ans;
    while(high >=low){
        int mid = (high+low)/2;
        int midsq = mid*mid;
        if(midsq == num)
            return mid;
        if(midsq > num)
            high = mid-1;
        else{
            low = mid+1;
            ans = mid;
        }
    }
    return ans;
}
 
int main(){
    int num;
    std :: cout << "Enter the number for finding square root : ";
    std :: cin >> num;
    int sqr = sqroot(num);
    std :: cout <<"The square root of the number is : " << sqr << std :: endl;

    return 0;
}