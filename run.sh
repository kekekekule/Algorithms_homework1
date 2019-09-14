#!/bin/bash
for i in 0{1..9} {10..60}
    do
        if [ i \< 10 ]
        then
            python3 main.py "0$i"
            python3 check.py "0$i.in" "0$i.out"
        else
            python3 main.py $i
            python3 check.py $i.in $i.out
        fi
    done
