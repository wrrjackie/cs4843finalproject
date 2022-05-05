from google.cloud import bigquery
import os

credentials_path = r"C:\Users\jacki\OneDrive\Documents\School\spring2022\cs4843 - Cloud Computing\final project\tranquil-bazaar-345200-820af1b331f7.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()

print("This program finds 2022 NFL Prospects of SELECTED POSITION with RAS scores of >9")
print("\nList of POSITIONS: CB - DE - DT - FB - FS - LB - LS - OC - OG - OT - PK - QB - RB - SS - TE - WR")
print("Cornerback - Def. End - Def. Tackle - Full Back - Free Safety - Linebacker - Long Snapper - Off. Center")
print("Off. Guard - Off. Tackle - Punt Kicker - Quarterback - Running Back - Strong Safety - Tight End - Wide Receiver")

position = input("\nPosition to search: ")

var = {
    "pos": position
}

query = """
    SELECT Name, College, RAS
    FROM `tranquil-bazaar-345200.NFL_Draft_RAS.NFL_Draft_RAS`
    WHERE POS = '%(pos)s'
    AND RAS > 9
    LIMIT 100
""" % var

query_job = client.query(query)
data = query_job.result()
rows = list(data)

print("\nResults:")
for r in rows:
    print(r[0] + " - " + r[1] + " - " + str(r[2]))