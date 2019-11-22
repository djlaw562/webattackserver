#web attack 
#usr/bin/python 2.7 (allowing user to know what version to use)

import urllib2.sys
#will automatically adapt imports when converting your sources to Python 3.

host = sys.argv [1] #first arugment for the host
dfile = sys.argv[2] #dictionary file cast

data = open(dfile,"r")	
fdata = data.readlines()
#purpose is to make the data to read teh dfile in a loop and read each line.

#for line to read each data 
for line in fdata:
#example use this on terminal (python example7.py http://localhost dir.txt
	linewn = line.strip("\n") #meant for printing results
	strreq = "{0}/{1}".format(host,linewn)
	#0 is host 1 is the file name to format the host and the line terminator
	#print 	strreq 
	try:
		#req = urllib2.urlopen(strreq)
#Use this on terminal to test again python example7.py http://localhost dir.txt
		if req.code == 200: #finding the file 
			print "[+] {0}/{1} is found (200)" .format(host,linewn)
			#priting a file that is already existing 
	except:
		pass 
		
#this will print out the directory information with the 200 response code
#code 200 is target request has succeeded. the information with the response is dependent used in request.
