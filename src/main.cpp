#include <iostream>
#include <string>
#include <vector>
#include <random>
#include <cstdint>
#include <chrono>
#include "sort.hpp"

 void init_vector_test1(std::vector<int> &v, int nbr_valeur, int min, int max){
    static std::random_device rd;
    static std::mt19937 gen(rd()); 
    std::uniform_real_distribution<double> distrib(min , max);
    //std::cout <<"Min:␣"<<min <<"␣Max:␣"<<max <<std::endl;
    v.clear();
    for( int i=0; i<nbr_valeur; i++){
        int random = static_cast<int>(round(distrib(gen)));
        v.push_back(random);
    }
}

void init_vector_test2(std::vector<int> &v,int nbr_valeur,int min,int max){
    v.clear();
    for(int i=0; i<nbr_valeur/2;i++){
        v.push_back(i);
    }
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_real_distribution<double> distrib(min , max);
    for( int i=nbr_valeur/2; i<nbr_valeur; i++){
        int random = static_cast<int>(round(distrib(gen)));
        v.push_back(random);
    }
}

void init_vector_test3(std::vector<int> &v,int nbr_valeur,int min,int max){
    v.clear();
    for(int i=0; i<nbr_valeur/2;i++){
        v.push_back(nbr_valeur-i);
    }
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_real_distribution<double> distrib(min , max);
    for( int i=nbr_valeur/2; i<nbr_valeur; i++){
        int random = static_cast<int>(round(distrib(gen)));
        v.push_back(random);
    }
}

int main(int argc,char *argv[]){
    if(argc!=3){
        std::cerr<<"Erreur nbr d'arguments"<<std::endl;
        return -1;
    }
    std::vector<int> v;
    int n=atoi(argv[1]);
    int numero_test=atoi(argv[2]);
    if(numero_test==1){
        init_vector_test1(v, n, 0, n);
    }
    else if(numero_test==2){
        init_vector_test2(v,n,0,n);
    }
    else if(numero_test==3){
        init_vector_test3(v,n,0,n);
    }
    else{
        std::cerr<<"Erreur numero test"<<std::endl;
        return -2;
    }
    std::chrono::steady_clock::time_point t_start=std::chrono::steady_clock::now();
    sort(v);
    std::chrono::steady_clock::time_point t_end =std::chrono::steady_clock::now();
    size_t temps_execution=std::chrono::duration_cast <std::chrono::microseconds>(t_end-t_start).count();
    std::cout<<n<<" "<<temps_execution<<std::endl;

    return 0;
}