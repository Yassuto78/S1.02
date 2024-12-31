#include "sort.hpp"
#include <algorithm>

void sort(std::vector<int> &v){
    int taille=v.size();
    for(int i = 1; i < taille; i++){
        int tmp=v[i];
        int j=i-1;
        for(;j>=0;j--){
            if(v[j]>tmp){
                v[j+1]=v[j];
            }
            else{
                break;
            }
        }
        v[j+1]=tmp; 
    }
}