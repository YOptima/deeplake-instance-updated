from google.cloud import bigquery

def print_query():
    client = bigquery.Client()
    query = 'SELECT count(*) size FROM `deeplake.datalake.dv360_data_maintable` WHERE Date = DATE_ADD(CURRENT_DATE(), INTERVAL -2 DAY)'
    job = client.query(query)
    result = job.result()
    for row in result:
        count=row.size
    print(count)

if __name__ == "__main__":
    print_query()
