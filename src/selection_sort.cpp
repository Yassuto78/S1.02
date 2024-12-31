#include "sort.hpp"
#include <algorithm>

void swap(int &a, int &b){
    int tmp=a;
    a=b;
    b=tmp;
}

void sort(std::vector<int> &v){
    int taille = v.size();
    for(int i = 0; i<taille - 1; i++){
        int min_actuel = i; //indice de la valeur minimum
        for(int j = i + 1; j < taille; j++){
            if(v[j] < v[min_actuel]){
                min_actuel=j; //si j'ai trouvé unn élément dans la suite dans mon tableau, il devient le min_actuel
            }
        }
        if(min_actuel != i){
            swap(v[i],v[min_actuel]);
        }
    }  
}