# -*- coding: cp1252 -*-
import urllib2, json, base64
accesstoken = "CPB5SKS9THM69NYFAKMK"
institution = "10007772"
page = 0
course = "U56119"
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(institution, course)
request = urllib2.Request(url)
request.add_header("Authorization", "Basic " + base64.encodestring(accesstoken+":").replace('\n',''))
response = urllib2.urlopen(request)
data = json.load(response)
#print json.dumps(data, indent=2)

for c in data:
    if c['Code']=="SALARY":
        i=c['Details']
        for x in i:
            if x['Code']=="MED":
                 print "The median salary in the sector for software enginerring students from Napier is "+str(x['Value'])

for c in data:
    if c['Code']=="SALARY":
        i=c['Details']
        for x in i:
            if x['Code']=="LDMED":
                 print "The median salary in the sector for software engineering graduates 40 months after graduation"+str(x['Value'])

for c in data:
    if c['Code']=="NSS":
        i=c['Details']
        for x in i:
            if x['Code']=="Q1":
                 print "The proportion of software engineering students who agree or strongly agree with the statement “Staff are good at explaining things is"+str(x['Value']) 
