#include <iostream>
#include <string>
#include <stdlib.h> 
#include <cmath>
#include <cstdio>

using namespace std;

int main(void) {
    string alph, heard;
    cin >> alph >> heard;
    string hummed="";
    for(int numhums=1;true;numhums++){
        hummed+=alph;
        int idx=0;
        for(int i = 0 ; i<hummed.size() && idx<heard.size(); i++){
            if (hummed[i]==heard[idx]){
                idx+=1;
            }
        }
        if(idx==heard.size()){
            cout<<numhums<<endl;
            return 0;
        }
        
    }
    
}
