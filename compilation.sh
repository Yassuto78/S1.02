#!/usr/bin/bash

rm -f data/*
g++ -Wall -Ofast -o bin/main.o -c src/main.cpp 
for alg in   stdsort stable_sort  #qsort insertion_sort  selection_sort bubble_sort
do
    echo alg:$alg
    g++ -std=c++17 -Wall -Ofast -o bin/$alg.o -c src/$alg.cpp 
    g++ -std=c++17 -Wall -Ofast -o bin/$alg bin/main.o bin/$alg.o
    for t in $(seq 1 3)
    do
        for i in $(seq 1 100)
        do
            n=${i}000
            echo $alg $n $t
            timeout 10m bin/$alg $n $t >> data/$alg$t.data
            return_code=$?
            if [[ $return_code -gt 120 ]]
            then
                echo "Temps d'execution maximal depassé pour ${alg} et ${t}"
                break
            fi      
        done
    done
done
#echo "Creation des plots"
cd src 
sage plot.sage.py