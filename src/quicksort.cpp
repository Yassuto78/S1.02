#include "sort.hpp"


void sort(std::vector<int> &v){
    if(v.size() >= 1){
        int pivot = v[0];
        std::vector<int> v1,v2,v3;
        for(int x : v){
            if(x < pivot){
                v1.push_back(x);
            }
            else if(x > pivot){
                v3.push_back(x);
            }
            else{
                v2.push_back(x);
            }
            sort(v1);
            sort(v3);
            v=v1;
            v.insert(v.end(),v2.begin(),v2.end());
            v.insert(v.end(),v3.begin(),v3.end());
        }
    }
}