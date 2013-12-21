#!/bin/bash
for thing in `find . -type l`; do
    echo $thing "-->" `readlink $thing`
done
