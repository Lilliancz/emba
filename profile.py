# Load the jinja library's namespace into the current module.
import jinja2
#this section sets up the csv for reading
import csv
import os

getinput = input("Enter the source filename (without the csv extension): ")
filename = getinput+'.csv'

#REMEMBER THAT THE SOURCE FILE MUST BE SORTED BY FACULTY AND TEAM AND THE 
#AVERAGE MUST ALSO BE MERGED IN AS THE LAST ENTRY

#open file and read it in as csv
f = open(filename, 'rt')
reader = csv.reader(f)
headers = next(reader)
column = {}
for h in headers:
    column[h] = []
for row in reader:
    for h, v in zip(headers, row):
        column[h].append(v)

import pdfkit	

#initialize the report text
concat = ""

#count rows of data in csv
rows = sum(1 for line in open(filename))
lastrow = rows-1

for i in range(0,lastrow):
#for i in range(0,5):
	FormalNamei = column["FormalName"][i]
	print(str(i) + column["FormalName"][i])

	# if this is the first instance of the subject
	concat = ""
	templateLoader = jinja2.FileSystemLoader( searchpath="templates" )
	templateEnv = jinja2.Environment( loader=templateLoader )
	#page1
	TEMPLATE_FILE = "profile.html"
	template = templateEnv.get_template( TEMPLATE_FILE )
	# Specify any input variables to the template as a dictionary.
	templateVars = { 
		"BusinessAddress":column["BusinessAddress"][i],
		"Company":column["Company"][i],
		"CompanyDescription":column["CompanyDescription"][i],
		"CompanyWebsite":column["CompanyWebsite"][i],
		"Education":column["Education"][i],
		"Email":column["Email"][i],
		"FormalName":column["FormalName"][i],
		"HomeCity":column["HomeCity"][i],
		"JobTitle":column["JobTitle"][i],
		"LeisureActivities":column["LeisureActivities"][i],
		"PreferredName":column["PreferredName"][i],
		"PreferredPhone":column["PreferredPhone"][i],
		"PreviousExp":column["PreviousExp"][i],
		"PrimaryResp":column["PrimaryResp"][i],
		"ProfessionalInterests":column["ProfessionalInterests"][i],
		"PhotoURL":column["PhotoURL"][i],
		"WorkEmail":column["WorkEmail"][i]
	}			 
	# Finally, process the template to produce our final text.
	outputText = template.render( templateVars )
	concat = concat + outputText	

	concat = concat + "</table></body></html>"
	#outputName = 'C:/Users/lillianc/Desktop/qualtrics/emba/2020Profiles/'+column["FormalName"][i] + ".html"
	#if not os.path.exists(os.path.dirname(outputName)):
	#	os.makedirs(os.path.dirname(outputName))
	#with open(outputName, 'w') as f:
	#	f.write(concat)
	outputPDF = 'C:/Users/lillianc/Desktop/qualtrics/emba/2020Profiles/'+column["FormalName"][i] + ".pdf"
	path_wkthmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
	config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

	pdfkit.from_string(concat, outputPDF, configuration = config)

