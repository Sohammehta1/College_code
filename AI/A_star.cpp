#include<iostream>
#include<map>
using namespace std;

string places[] = {"katraj", "bibvewadi", "sahakarnagar", "parvati", "lokmanyanagar", "sinhgad_rd","kothrud"};
int h_vals[] = {10,8,7,5,3,2,0};
map<string, int> h_n;
map<string, map<string,int>> g_n;

class Find_path{
    map<string, int> h_n;
    map<string, map<string,int>> g_n;
    Find_path(){
        
    }
};




int main(){
    cout << "Hello world!" << endl;
    return 0;
}