#!/bin/bash
if [ $# == 1 ]
then
git config --global user.email robertsandersons269@gmail.com
git add .
#git commit -m "20180925"
git commit -m $1
#git pull
git push origin master
fi

