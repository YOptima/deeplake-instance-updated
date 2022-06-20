#!/bin/sh

curr_date=$(date '+%d%m%Y')
sudo python3 transform_isolation_report.py $1 $2
sudo gsutil cp $1.csv gs://deeplake
sudo rm -f $1*
echo -e "Triggered Cloud Function to upload TOD tabel data triggered"
sleep 10
sudo python3 transform_isolation_report.py $3 $4
sudo gsutil cp $3.csv gs://deeplake
sudo rm -f $3*
echo -e "Triggered Cloud Function to upload TOD with 1hrTTC tabel data triggered"
sleep 10
sudo python3 transform_isolation_report.py $5 $6
sudo gsutil cp $5.csv gs://deeplake
sudo rm -f $5*
echo -e "Triggered Cloud Function to upload category tabel data triggered"
sleep 10
echo -e "Triggered Cloud Function to upload pixel load with order id tabel data triggered"
sudo python3 transform_isolation_report.py $7 $8
sudo gsutil cp $7.csv gs://deeplake
sudo rm -f $7*
echo -e "Triggered Cloud Function to upload channel tabel data triggered"
sleep 20
sudo gsutil cp lock_isolation gs://trigger-isolation
echo -e "Triggered Cloud Function to update ttc data to TOD table triggered"

num=$(ls lock_* | wc -l)
if [ $num -eq 46 ]
then
    sudo gcloud compute instances stop deeplake --zone us-west1-b
fi
