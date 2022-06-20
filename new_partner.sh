#!/bin/sh


sudo python3 export_api.py --query_id 906769432
sudo python3 transform_partner_report.py 906769432
sudo python3 new_partner.py
