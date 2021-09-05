# Analyse JSON data downloaded from reed.co.uk API to determine the most popular words used

# Resources
# https://mkyong.com/python/python-how-to-split-a-string/
# https://www.youtube.com/watch?v=daefaLgNkw0
# https://www.delftstack.com/howto/python/remove-special-characters-from-string-python/
# https://stackoverflow.com/questions/17839973/constructing-pandas-dataframe-from-values-in-variables-gives-valueerror-if-usi
# https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.transpose.html
# https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/#:~:text=In%20Python%2C%20lower()%20is,it%20returns%20the%20original%20string.

# Import libraries
import json
import pandas as pd

# Import data from file
with open('json_results.txt') as f:
    data = json.load(f)
f.close()
#print(data)

# Build a list containing all the words in the descriptions
words = []
for job in data['results']:
    string = job['jobDescription'].split(" ")
    words = words + string

#print(string)
#print(words)
#print(len(words[0]))

# Remove special characters from words and convert to lowercase
word_count = len(words)
for idx in range(word_count):
    word = words[idx].lower()
    words[idx] = ''.join(filter(str.isalnum, word))
    #print(''.join(filter(str.isalnum, word)))

# Count the words using a dictionary
word_count = dict()
for word in words:
    if len(word) > 1:
        #print('word_count', word_count.get(word))
        if word_count.get(word) != None:
            word_count[word] += 1
            #print('Found!')
        else:
            #print('not found')
            word_count[word] = 1
            pass

#print(word_count)


# Convert  into dataframe
df = pd.DataFrame(word_count, index=[0])

# Transpose dataframe
df = df.transpose(copy=False)
print(df)

#export dataframe to excel
df.to_excel(r'C:\Users\donnp\source\repos\Reed job analysis\word_count_export.xlsx', header=False)
