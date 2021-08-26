#!/bin/bash

for f in *.bag.active; do 
    mv -- "$f" "${f%.bag.active}.bag"
done
