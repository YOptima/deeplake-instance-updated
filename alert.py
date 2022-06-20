from google.cloud import bigquery

client = bigquery.Client()
query1 = ' SELECT Advertiser_ID adv, sum(Impressions) imps FROM `deeplake.datalake.dv360_data_maintable` WHERE date = "2020-10-12" Group by Advertiser_ID '
query2 = ' SELECT Advertiser_ID adv, Impressions imps FROM `deeplake.datalake_temp.data_validation` '
job1 = client.query(query1)
job2 = client.query(query2)
result1 = job1.result()
result2 = job2.result()

for row1,row2 in zip(result1,result2):
    if row1.adv==row2.adv:
        imp1=row1.imps
        imp2=row2.imps
        print(imp1,imp2)
