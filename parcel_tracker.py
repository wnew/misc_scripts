import os, urllib, sys
from optparse import OptionParser

p = OptionParser()
opts, args = p.parse_args(sys.argv[1:])

if args==[]:
   print "Enter a file to read the tracking numbers from"
   exit()


packages = []

with open(args[0],'r') as f:
    packages = f.readlines()

url = 'http://sms.postoffice.co.za/TrackingParcels/Parcel.aspx?id='

for package in packages:
   f = open(urllib.urlretrieve(url+package)[0],'r')
   html = f.read()
   if "could not be found in our database" in html:
      print package + " could not be found"
   else:
      print package + " " + html.split("local Item number: </b>")[1].split("\n")[0].replace("<b>","").replace("</b>","").replace("</font>","").replace("</td>","")[:-1] + " at " + html.split("Location last scanned: ")[1].split("\n")[0].replace("<b>","").replace("</b>","").replace("</font>","").replace("</td>","")
   f.close()

