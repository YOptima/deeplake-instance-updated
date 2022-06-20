#!/bin/sh

sudo bq extract 'deeplake:mapping.dv3_app_url_mapping' gs://test_ankit/App_URL_ID.csv
sudo bq extract 'deeplake:mapping.dv3_city_region_dma_mapping' gs://test_ankit/City_ID.csv
sudo bq extract 'deeplake:mapping.dv3_creative_mapping' gs://test_ankit/Creative_ID.csv
sudo bq extract 'deeplake:mapping.dv3_exchange_inventory_mapping' gs://test_ankit/Exchange_ID.csv
sudo bq extract 'deeplake:mapping.dv3_isp_mapping' gs://test_ankit/Exchange_ID.csv
sudo mv 801086366.csv Ad_Position.csv
sudo mv 801086228.csv Country.csv
sudo mv 801086122.csv Position_in_Content.csv
sudo mv 801085503.csv Creative_Size.csv
sudo mv 801084952.csv Video_Player_Size.csv
sudo mv 801083962.csv Environment.csv

for dim in "App_URL_ID" "City_ID" "Region_ID" "Creative_ID" "Exchange_ID"; do
    sudo gsutil cp gs://test_ankit/${dim}.csv .
    sudo python3 update_1d_mapping.py $dim
    sudo gsutil cp ${dim}_1d.csv gs://test_ankit
    sudo bq load --source_format CSV --skip_leading_rows 1 --allow_jagged_rows _datalake.dv3_1d_mapping gs://test_ankit/${dim}_1d.csv
done

for dim in "Ad_Position" "Country"  "Position_in_Content" "Creative_Size" "Video_Player_Size" "Environment"; do
    sudo python3 update_1d_mapping.py $dim
    sudo gsutil cp ${dim}_1d.csv gs://test_ankit
    sudo bq load --source_format CSV --skip_leading_rows 1 --allow_jagged_rows _datalake.dv3_1d_mapping gs://test_ankit/${dim}_1d.csv
done
