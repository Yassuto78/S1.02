#include "sort.hpp"
#include <cstdlib>

int comparateur(const void *a, const void *b){
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
 
    if (arg1 < arg2){
        return -1;
    }
    if (arg1 > arg2){
        return 1;
    }
    return 0;
}

void sort(std::vector<int> &v){
 std::qsort(&v[0], v.size(), sizeof(int), comparateur);
}