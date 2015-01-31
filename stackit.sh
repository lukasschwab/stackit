#!/bin/bash

while getopts ":s:" opt; do
    case "$opt" in
        s)
            python stackit-core.py $2
            ;;
        \?)

            ERROR=$(($2 $3 >&2) 2>&1)

            echo="ERROR=$ERROR"

            python stackit-core.py -stderr $ERROR$
            ;;
       
    esac
done
