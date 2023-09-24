#!/usr/bin/env bash

pattern1="..H."
file1="all04.txt"
file2="all06.txt"

egrep $pattern1 $file1 | while read player1
do 
   letter=$(echo $player1 |cut -c1 | sort -u)
   pattern2=$letter"...I."
   player2=$(egrep $pattern2 $file2)
   if [ $? == 0 ]
     then echo $player1 $player2
   fi
done
