# Analyse JSON data downloaded from reed.co.uk API and convert it to a dataframe and Excel workbook

# Resources
# https://www.youtube.com/watch?v=9N6a-VLBa2I
# https://datatofish.com/dictionary-to-dataframe/
# https://www.youtube.com/watch?v=ohCDWZgNIU0
# https://www.youtube.com/watch?v=mJ3IiOjmY-M&t=321s
# https://www.youtube.com/watch?v=pTT7HMqDnJw
# https://datatofish.com/export-dataframe-to-excel/

# Import libraries
import json
import pandas as pd

# Import data from file
with open('json_results.txt') as f:
    data = json.load(f)
f.close()
#print(data)

# Make a new dictionary with data in tabular format
new_dict = {}
jobIds = []
employers = []
locations = []
jobTitles = []
descriptions = []
for job in data['results']:
    jobIds.append(job['jobId'])
    employers.append(job['employerName'])
    locations.append(job['locationName'])
    jobTitles.append(job['jobTitle'])
    descriptions.append(job['jobDescription'])

new_dict['jobId'] = jobIds
new_dict['employer'] = employers
new_dict['location'] = locations
new_dict['jobTitle'] = jobTitles
new_dict['description'] = descriptions
print(new_dict)

# Convert  into dataframe
df = pd.DataFrame(new_dict)
#print(df)

#export dataframe to excel
df.to_excel(r'C:\Users\donnp\source\repos\Reed job analysis\dataframe_export.xlsx', index=False, header=True)
