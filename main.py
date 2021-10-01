import re
import sys
from google.cloud import storage
from prettytable import PrettyTable
import pandas as pd
BUCKET = 'test_buc_for_proj' #add bucket name

# Create a Cloud Storage client.
gcs = storage.Client()
testcase1="test_buc_for_proj/incoming/medxcel/" # add test case path i.e test_buc_for_proj/incoming/medxcel
bucket = gcs.get_bucket(BUCKET)
accesslist_1=[]
def my_list_bucket(bucket_name,testcase1):
    accesslist=[]
    test_scenario="[SIT_Medxcel_001] - To validate the GCS storage bucket location, Bucket Name and Folder Name for Medxcel source incoming file"
    accesslist.append(test_scenario)
    spli=test_scenario.split("-")
    spli=spli[0]
    test_id=spli
    accesslist.append(test_id)
    a_bucket = gcs.lookup_bucket(bucket_name)
    bucket_iterator = a_bucket.list_blobs()
    for resource in bucket_iterator:
        res=bucket_name+"/"+resource.name
        if res==testcase1:
            expexted_result=res

    accesslist.append(testcase1)
    accesslist.append(expexted_result)
    
    if expexted_result==testcase1:
        accesslist.append(expexted_result)
        accesslist.append("passed")
    for i in accesslist:
        accesslist_1.append(i)
  
my_list_bucket(BUCKET,testcase1)

api=[]
print(accesslist_1)
for i in accesslist_1:
    api.append(i)
len_api=len(api)

table = PrettyTable()


for i in range(0,len_api):
    table.add_row(api[i])

dew_table1=pd.DataFrame(api)

print(dew_table1)
