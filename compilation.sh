#!/usr/bin/bash

rm data/*
g++ -Wall -Ofast -o bin/main.o -c src/main.cpp 
#TODO: ajouter les algorithme choisi et les coder 1,2,4,5,6,7 (implementer la fonction sort)
for alg in stdsort stable_sort
do
    echo alg:$alg
    g++ -Wall -Ofast -o bin/$alg.o -c src/$alg.cpp 
    g++ -Wall -Ofast -o bin/$alg bin/main.o bin/$alg.o
    for t in $(seq 1 5)
    do
        echo $t $alg
        #TODO: Renvoyez les bons format de donées 
        timeout 10m bin/$alg >> data/$alg$t.data
        return_code=$?
        echo return_code=$return_code
        #TODO: traiter le return code
    done
done