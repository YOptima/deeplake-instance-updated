import json
import argparse
import dv3_scheduler as dv3

def update_json(partner_id,config):
    with open(config, "r") as jsonFile:
        data = json.load(jsonFile)
    data["schedule"]["endTimeMs"] = "1750000000000"
    type = {"type":"FILTER_PARTNER","value":partner_id}
    data["params"]["filters"].append(type)

    response = dv3.scheduleReports(data)
    #print(data)
    #response = '123'
    return response
