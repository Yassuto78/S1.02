#include "sort.hpp"
#include <algorithm>

void swap(int &a, int &b){
    int tmp=a;
    a=b;
    b=tmp;
}

void sort(std::vector<int> &v){
    int taille = v.size();
    bool changement;
    do{
        changement=false;
        for(int i=0; i<taille-1;i++){
          if (v[i]>v[i+1]){
            swap(v[i],v[i+1]);
            changement=true;
          }     
        }
    }while(changement);
}