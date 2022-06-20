#!/bin/sh

curr_date=$(date '+%d%m%Y')
sudo gsutil cp $1_$curr_date.csv gs://deeplake_rawdata
sudo python3 transform_mapping_report.py $1 $2
sudo gsutil cp $1.csv gs://deeplake
sudo rm -f $1*
echo -e "Triggered Cloud Function to upload app/url mapping table data triggered"
sleep 10
sudo gsutil cp $3_$curr_date.csv gs://deeplake_rawdata
sudo python3 transform_mapping_report.py $3 $4
sudo gsutil cp $3.csv gs://deeplake
sudo rm -f $3*
echo -e "Triggered Cloud Function to upload city mapping tabel data triggered"
sleep 10
sudo gsutil cp $5_$curr_date.csv gs://deeplake_rawdata
sudo python3 transform_mapping_report.py $5 $6
sudo gsutil cp $5.csv gs://deeplake
sudo rm -f $5*
echo -e "Triggered Cloud Function to upload creative mapping tabel data triggered"
sleep 10
sudo gsutil cp $7_$curr_date.csv gs://deeplake_rawdata
sudo python3 transform_mapping_report.py $7 $8
sudo gsutil cp $7.csv gs://deeplake
sudo rm -f $7*
echo -e "Triggered Cloud Function to upload ISP mapping tabel data triggered"
sleep 10
sudo gsutil cp $9_$curr_date.csv gs://deeplake_rawdata
sudo python3 transform_mapping_report.py $9 ${10}
sudo gsutil cp $9.csv gs://deeplake
sudo rm -f $9*
echo -e "Triggered Cloud Function to upload Exchange mapping tabel data triggered"
sleep 10
sudo gsutil cp ${11}_$curr_date.csv gs://deeplake_rawdata
sudo python3 transform_mapping_report.py ${11} ${12}
sudo gsutil cp ${11}.csv gs://deeplake
sudo rm -f ${11}*
echo -e "Triggered Cloud Function to upload Entity mapping tabel data triggered"
sudo python3 transform_li_mapping.py 884590714
sudo bq load --source_format CSV --skip_leading_rows 1 --allow_jagged_rows --replace mapping.dv3_li_mapping 884590714.csv
sudo rm -f 884590714*
sudo gsutil cp lock_mapping gs://trigger_mapping
sudo gsutil cp lock_mapping gs://trigger-entity_mapping
echo -e "Triggered Cloud Function to update all the mapping table triggered"
sudo python3 instance_stop.py
