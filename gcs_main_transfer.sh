#!/bin/sh

curr_date=$(date '+%d%m%Y')
sudo gsutil cp $1_$curr_date.csv gs://deeplake_rawdata
sudo python3 data_transformation.py $1
sudo gsutil cp $1.csv gs://deeplake
echo -e "Cloud Function to upload 19D data triggered"
sudo rm -f $1*
sleep 100
sudo gsutil cp $2_$curr_date.csv gs://deeplake_rawdata
sudo python3 data_transformation.py $2
sudo gsutil cp $2.csv gs://deeplake
echo -e "Cloud Function to upload ttc data triggered"
sudo rm -f $2*
sleep 30
sudo gsutil cp 734229253_$curr_date.csv gs://deeplake_rawdata
sudo python3 drop_column.py
sudo gsutil cp 734229253.csv gs://deeplake
echo -e "Cloud Function to upload Advertiser map data triggered"
sudo rm -f 734229253*
sleep 30
sudo gsutil cp lock gs://trigger-ttc
echo -e "Cloud Function to upldate ttc and advertiser details to main table triggered"
sudo gsutil cp 738307542_$curr_date.csv gs://deeplake_rawdata
sudo python3 validation_report.py 738307542
sudo gsutil cp 738307542.csv gs://deeplake
sudo rm -f 738307542*
echo -e "Cloud Function to upload validation data"
sudo python3 instance_stop.py
