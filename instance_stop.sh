#!/bin/sh


num=$(ls lock_* | wc -l)
# if [ $num -eq 57 ]
if [ $num -eq 100 ]
then
    sudo gcloud compute instances stop deeplake --zone us-west1-b
fi
