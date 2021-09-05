# Reed job analysis
The purpose of this project is to extract job data from Reed.co.uk via their API and perform a custom keyword search using Python.
There are two key objectives:
1. Search a large volume of jobs to find specific keywords that would not be found with the standard Reed web search functionality
1. Potentially build a project that can be used as part of my data analysis portfolio

# Steps 
1. Register with Reed to get API key
2. Build a basic API call in Postman to test if API key is working
3. Customise the Postman API call to find desired jobs
4. Export the API results from postman into a new JSON file
5. Manipulate the JSON file with python to get it into table format
6. Perform a word search on the tabular data to identify the most common words
6. Build a Power BI dashboard to visualise the most common keywords
7. Check alignment between word search and CV and update CV to form a comprehensive overview that includes most popular words
8. Search for custom keywords and identify relevant job postings
9. Share results on LinkedIn via a post

# Documentation
- The Python code will be stored on github
- The API calls will be stored in Postman and documented further down in this document
- The API key is not saved to github for security reasons
- Visualisation is done in Power Bi

# How to make API calls in Postman
1. Create a new GET request
1. Create the URL for example: https://www.reed.co.uk/api/1.0/search?keywords=analyst&location=london
1. In the Authorisation tab, selected type of authorisation as Basic Auth
1. For the username, enter the API key
1. Leave the password blank
1. Run the request

The generic syntax for URL is: https://www.reed.co.uk/api/{versionnumber}/search?keywords={keywords}&locationName={locationName}&employerId={employerId}&distanceFromLocation={distance in miles}
See https://www.reed.co.uk/developers/jobseeker for more details.

# Using the Python program for generating Excel spreadsheet and updating Power Bi dashboard
The Python program transforms data from the API call into an Excel spreadsheet. Here are the steps to follow to create the Excel spreasheet:
1. In Postman, make a call to the API as described above
1. Copy the results of the call into the text file called 'json_results.txt'. Save and close the file
1. Run the Python program ('Reed-analysis.py'). Output is saved in 'dataframe_export.xlsx'
1. Open the Power Bi dashboard ('Reed_analysis.pbix') and on the Home tab, refresh the data

# Maniputations in Power BI
This section contains notes on some of the manipulations done on the Power Bi dashboard
Article on how to combine city and country fields: https://adatis.co.uk/power-bi-maps-handling-duplicate-city-names/.
How to created calculated fcolumns using measures: https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-tutorial-create-calculated-columns