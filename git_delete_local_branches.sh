#!/bin/bash
for branch in `git branch -a | grep remotes | grep -v HEAD | grep -v master`; do
    git branch -D $branch
done
