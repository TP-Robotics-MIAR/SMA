#!/bin/bash

read -p "Enter Array: " -a array

## print element
echo ${array[1]}
for element in $array;
do
	echo $element
done

