#include "sort.hpp"
#include <algorithm>

void sort(std::vector<int> &v){
    std::stable_sort(v.begin(),v.end());
}